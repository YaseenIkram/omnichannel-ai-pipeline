# OmniChannel AI Data Intake & Triage Pipeline

A production-ready data engineering pipeline designed to ingest unorganized, unstructured corporate communications (such as raw phone transcripts, customer support emails, and website contact form logs) from a local storage directory, extract critical business attributes using LLM programmatic inference, and compile them into a standardized, structured corporate database.

---

## 🚀 Key System Features

* **Automated Data Normalization:** Instantly translates chaotic human slang, unstructured phrasing, and casual monetary references (e.g., "around twenty-five thousand dollars, maybe up to 30k") into strict database types like pure integers.
* **Schema Enforcement & Validation:** Leverages Groq JSON-mode configurations to guarantee structured schema parsing, preventing data corruption or runtime structural errors.
* **Token Auditing & Footprint Visibility:** Tracks prompt and completion token allocations per file execution, providing exact infrastructure cost visibility and context window safety monitoring.
* **Zero-Dependency Testing Sandbox:** Features an integrated mock data generation layer to build complex, poorly-formatted text files on demand for immediate pipeline verification without exposing proprietary customer records.

---

## 🛠️ System Architecture Design

The codebase follows standard enterprise software design patterns, splitting system logic into isolated, modular files to optimize maintainability and scalability:

* `config.py`: The central configuration gatekeeper. Manages global constants, API target models, directory paths, and enforces secure terminal memory validation.
* `mock_data_generator.py`: A testing utility that programmatically constructs a directory of messy, multi-format log files simulating authentic corporate data profiles.
* `ai_processor.py`: The direct interface layer with the Llama 3 API. Constructs system/user payloads, defines structural parameters, handles strict extraction rules, and catches API exceptions.
* `main_pipeline.py`: The core data pipeline engine. Scans target folders, opens unformatted text streams regardless of file extension, maps payloads to the AI layer, and leverages Pandas to compile, order, and serialize a structured master file.

---

## 📦 Installation & Setup

Follow these steps to clone, configure, and initialize the system in your local Linux development environment:

### 1. Clone the Workspace
Clone the repository down to your machine and navigate into the root directory:
```bash
git clone [https://github.com/YaseenIkram/omnichannel-ai-pipeline.git](https://github.com/YaseenIkram/omnichannel-ai-pipeline.git)
cd omnichannel-ai-pipeline
```

### 2. Initialize a Virtual Environment
Isolate your project dependencies by building and activating a clean Python virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Production Dependencies
Install the heavy-duty data libraries required to power the processing engine:
```bash
pip install pandas requests
```

### 4. Mount API Credentials Securely
Mount your Groq API authentication key directly into your terminal's volatile memory. This keeps your private credentials completely safe and hidden from the public codebase:
```bash
export GROQ_API_KEY="your_actual_api_key_here"
```

---

## ⚙️ Running the Pipeline

Execute the master orchestration pipeline script to run the intake engine:
```bash
python3 main_pipeline.py
```

### Expected Runtime Output Flow
When triggered, the system automatically checks for existing intake records. If the target folders are missing, it initializes the mock data utility, sweeps the intake directory, and streams live processing telemetry directly into the standard output:

```text
=== STARTING ENTERPRISE DATA INTAKE PIPELINE ===
[SYSTEM] Found 3 target files inside intake folder.

Processing File: call_audio_trans_44102.log
  [METRICS] Tokens Used -> Prompt: 264 | Completion: 65
  [SUCCESS] Extracted record for: Robert Chen
--------------------------------------------------
Processing File: incoming_msg_99.txt
  [METRICS] Tokens Used -> Prompt: 251 | Completion: 60
  [SUCCESS] Extracted record for: super_skater99@gmail.com
--------------------------------------------------
Processing File: web_form_dump_alpha.data
  [METRICS] Tokens Used -> Prompt: 238 | Completion: 42
  [SUCCESS] Extracted record for: Amanda Ross
--------------------------------------------------

[PIPELINE COMPLETE] Generated structured database: 'unified_corporate_database.csv'
```

### Final Data Compilation Output
Once the pipeline exits cleanly, it compiles all analyzed profiles, structures them using Pandas, and outputs a standardized, production-ready dataset named `unified_corporate_database.csv` containing the following enforced column matrix:

| sender_name | organization | contact_channel | intent | financial_value | priority | source_file |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Robert Chen | Chen Manufacturing | Phone | Sales Lead | 12000 | High | call_audio_trans_44102.log |
| super_skater99... | Individual | Email | Refund Request | 49 | High | incoming_msg_99.txt |
| Amanda Ross | Individual | WebForm | Feedback | 0 | Low | web_form_dump_alpha.data |

---

## 🔒 Security & Data Governance
This repository implements strict data governance practices:
* **Credential Isolation:** No plain-text passwords or API tokens are hardcoded into the architecture. Authentication is performed natively via environment memory variables (`os.environ`).
* **Git Boundary Shields:** The configuration layer uses a `.gitignore` blueprint to actively block local development assets (`.venv/`), transient caches (`__pycache__/`), unstructured source logs (`raw_data_intake/`), and generated sheets (`.csv`) from ever leaking onto the public internet.
