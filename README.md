# IDAMP — Intent-Driven Agentic Medallion Pipeline

## Overview

IDAMP accepts raw CSV files plus a plain-English business question and produces an HTML executive report with Plotly charts backed by DuckDB SQL.

## Architecture

```text
Streamlit -> Supervisor -> Agents -> Storage
```

## Four Phases

| Phase | Focus | Output |
| --- | --- | --- |
| 1 | Profiler + Bronze STTM | Bronze STTM |
| 2 | Bronze load + Silver STTM | Silver STTM |
| 3 | Silver load + Gold STTM | Gold STTM |
| 4 | Gold + Reporter | HTML report |

## Medallion Layers

| Layer | What happens |
| --- | --- |
| Bronze | Ingestion and metadata |
| Silver | Cleaning, normalization, quality |
| Gold | Join/aggregation for reporting |
| Report | Business answer and chart rendering |

## What Makes This Agentic

THINK / INSPECT / PLAN / ACT / VERIFY

## Project Structure

```text
IDAMPorg/
├─ README.md
├─ requirements.txt
├─ test_import.py
├─ .env
├─ agents/
├─ app/
├─ core/
├─ tests/
├─ data/
├─ audit_logs/
├─ reports/
└─ .chroma/
```

## Agents

- `profiler.py`: profiles datasets.
- `sttm_generator.py`: creates STTM CSVs.
- `bronze_agent.py`: bronze ingestion.
- `silver_agent.py`: silver quality.
- `gold_agent.py`: gold transformation.
- `reporter.py`: report generation.

## Key Design Patterns

- Tool Factory + Closure
- Scratchpad pattern
- HITL gates
- ReAct loop
- Separation of Intelligence and Execution

## Tech Stack

| Component | Purpose |
| --- | --- |
| Streamlit | UI |
| LangChain | Agent orchestration |
| DuckDB | SQL analytics |
| Plotly | Charts |
| ChromaDB | Memory |

## Setup & Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Pipeline

```bash
streamlit run app/streamlit_app.py
```

## Configuration

See `core/config.py`.

## Observability

Traces are written to `data/traces`.

## FAQ

- Why 4 phases?
- Inspect vs execute?
- Scratchpad?
- Provider switch?
- Resume-on-failure?
- STTM location?
