"""Write an isolated folder with exactly what the LLM parser and decider stages see, for a stand-in LLM
(for example a subagent) to work from when no API key is available.

Usage: python3 tools/prep_llm_stage_inputs.py CASE_DIR OUT_DIR

OUT_DIR gets policy.txt, parser_instructions.md (prompt, actor-class list, JSON schema),
decider_instructions.md, record_for_decider.json (the case's fixture record, so decider answers can be
compared question by question) and questions.json. Nothing about outcomes is copied.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from praxeo import parser, vocabulary  # noqa: E402
from praxeo.decider import DECIDER_SYSTEM  # noqa: E402
from praxeo.questions import record_questions  # noqa: E402
from praxeo.schema import PolicyRecord  # noqa: E402


def main(case: Path, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    (out / "policy.txt").write_text((case / "policy.txt").read_text())
    (out / "parser_instructions.md").write_text(
        "# Parser task\n\n" + parser.instructions() +
        "\n\nWrite ONE JSON object to `record.json` in this folder that validates against the JSON Schema below "
        "(pydantic model PolicyRecord). Use only instrument names from this list: " +
        ", ".join(sorted(vocabulary.instruments())) + ". Quote source sentences exactly as they appear in policy.txt.\n\n"
        "```json\n" + json.dumps(PolicyRecord.model_json_schema(), indent=1) + "\n```\n")
    record = parser.parse_fixture(case / "record.json")
    questions = [q.model_dump() for _comp, q, _ in record_questions(record)]
    (out / "decider_instructions.md").write_text(
        "# Decider task\n\n" + DECIDER_SYSTEM +
        "\n\nAnswer every question in `questions.json` using `record_for_decider.json` and `policy.txt`. Write "
        "`answers.json`: a JSON list with one object per question, each with keys question_id (copied exactly), "
        "value (\"yes\" or \"no\"), probability (your probability that the answer is yes, 0 to 1), rationale "
        "(one or two sentences), evidence (list of record lines quoted exactly, may be empty).\n")
    (out / "record_for_decider.json").write_text(record.model_dump_json(indent=1))
    (out / "questions.json").write_text(json.dumps(questions, indent=1))
    print(out, len(questions), "questions")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
