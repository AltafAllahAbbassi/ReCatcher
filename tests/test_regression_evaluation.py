import json
from pathlib import Path
import tempfile
import textwrap
import unittest
from unittest.mock import patch

import pandas as pd

from ReCatcher.recatcher import ReCatcher
from ReCatcher.utils import execute_unittest


class ExecuteUnittestTests(unittest.TestCase):
    def run_suite(self, body):
        source = "import unittest\nclass TestCases(unittest.TestCase):\n"
        source += textwrap.indent(textwrap.dedent(body), "    ")
        return execute_unittest(source, timeout=5)

    def test_passing_suite(self):
        self.assertIs(self.run_suite("def test_value(self):\n    self.assertEqual(1 + 1, 2)"), True)

    def test_failed_assertion(self):
        self.assertIs(self.run_suite("def test_value(self):\n    self.assertEqual(1, 2)"), False)

    def test_test_exception(self):
        self.assertIs(self.run_suite("def test_value(self):\n    raise RuntimeError('test error')"), False)

    def test_syntax_error(self):
        self.assertIs(execute_unittest("def invalid(:", timeout=5), False)

    def test_missing_test_class(self):
        self.assertIs(execute_unittest("value = 1", timeout=5), False)

    def test_invalid_test_class(self):
        source = "class TestCases:\n    def test_value(self):\n        pass"
        self.assertIs(execute_unittest(source, timeout=5), False)

    def test_subprocess_exit_without_result(self):
        self.assertIs(execute_unittest("import os\nos._exit(1)", timeout=5), False)

    def test_timeout(self):
        self.assertIs(execute_unittest("import time\ntime.sleep(2)", timeout=0.1), False)


class GeneralLogicEvaluationTests(unittest.TestCase):
    @staticmethod
    def read_results(result_file):
        return [json.loads(line) for line in Path(result_file).read_text().splitlines()]

    def test_humaneval_summary_counts_successes(self):
        evaluator = ReCatcher.__new__(ReCatcher)
        evaluator.benchmark = [{"test": "def check(candidate):\n    assert candidate(2) == 3"}] * 3
        correct = "def candidate(value):\n    return value + 1"
        incorrect = "def candidate(value):\n    return value - 1"
        frame = pd.DataFrame({
            "task_id": ["task_0", "task_1", "task_2"],
            "prompt": ["Add one"] * 3,
            "exp_0": [correct, incorrect, incorrect],
        })

        with tempfile.TemporaryDirectory() as result_dir, patch(
            "ReCatcher.recatcher.tqdm", side_effect=lambda items: items
        ):
            result_file, summary = evaluator.test_general_logic_humaneval(frame, result_dir)
            rows = self.read_results(result_file)

        self.assertEqual(summary, {"exp_0": {"Correct code": 1}})
        self.assertEqual(len(rows), len(frame))
        self.assertEqual([row["correct_code"] for row in rows], [True, False, False])
        self.assertEqual([row["task_id"] for row in rows], frame["task_id"].tolist())

    def test_bigcode_evaluates_all_rows_and_counts_successes(self):
        for n_rows, passing_rows in [(3, {1}), (6, {1, 4})]:
            with self.subTest(n_rows=n_rows):
                evaluator = ReCatcher.__new__(ReCatcher)
                evaluator.benchmark = [{"test": ""}] * n_rows
                outcomes = [i in passing_rows for i in range(n_rows)]
                frame = pd.DataFrame({
                    "task_id": [f"task_{i}" for i in range(n_rows)],
                    "prompt": ["Test placeholder"] * n_rows,
                    "exp_0": [f"candidate_{i}" for i in range(n_rows)],
                })

                with tempfile.TemporaryDirectory() as result_dir, patch(
                    "ReCatcher.recatcher.tqdm", side_effect=lambda items: items
                ), patch(
                    "ReCatcher.recatcher.execute_unittest", side_effect=outcomes
                ) as execute:
                    result_file, summary = evaluator.test_general_logic_bigcode_bench(frame, result_dir)
                    rows = self.read_results(result_file)

                self.assertEqual(execute.call_count, n_rows)
                self.assertEqual(summary, {"exp_0": {"Correct code": len(passing_rows)}})
                self.assertEqual(len(rows), n_rows)
                self.assertEqual([row["correct_code"] for row in rows], outcomes)
                self.assertEqual([row["task_id"] for row in rows], frame["task_id"].tolist())
                self.assertEqual([row["code"] for row in rows], frame["exp_0"].tolist())


if __name__ == "__main__":
    unittest.main()
