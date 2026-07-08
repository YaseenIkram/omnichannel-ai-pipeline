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

```text
omnichannel-ai-pipeline/
├── .gitignore                  # Invisible security shield preventing data leaks
├── README.md                   # Comprehensive system documentation
├── config.py                   # Central infrastructure configuration gateway
├── ai_processor.py            # LLM programmatic interface and payload manager
├── mock_data_generator.py      # Automated testing data sandbox utility
└── main_pipeline.py            # Core engine orchestrating files and Pandas structures
config.py: The central configuration gatekeeper. Manages global constants, API target models, directory paths, and enforces secure terminal memory validation.mock_data_generator.py: A testing utility that programmatically constructs a directory of messy, multi-format log files simulating authentic corporate data profiles.ai_processor.py: The direct interface layer with the Llama 3 API. Constructs system/user payloads, defines structural parameters, handles strict extraction rules, and catches API exceptions.main_pipeline.py: The core data pipeline engine. Scans target folders, opens unformatted text streams regardless of file extension, maps payloads to the AI layer, and leverages Pandas to compile, order, and serialize a structured master file.📦 Installation & SetupFollow these steps to clone, configure, and initialize the system in your local Linux development environment:1. Clone the WorkspaceClone the repository down to your machine and navigate into the root directory:Bashgit clone [https://github.com/YaseenIkram/omnichannel-ai-pipeline.git](https://github.com/YaseenIkram/omnichannel-ai-pipeline.git)
cd omnichannel-ai-pipeline
2. Initialize a Virtual EnvironmentIsolate your project dependencies by building and activating a clean Python virtual environment:Bashpython3 -m venv .venv
source .venv/bin/activate
3. Install Production DependenciesInstall the heavy-duty data libraries required to power the processing engine:Bashpip install pandas requests
4. Mount API Credentials SecurelyMount your Groq API authentication key directly into your terminal's volatile memory. This keeps your private credentials completely safe and hidden from the public codebase:Bashexport GROQ_API_KEY="your_actual_api_key_here"
⚙️ Running the PipelineExecute the master orchestration pipeline script to run the intake engine:Bashpython3 main_pipeline.py
Expected Runtime Output FlowWhen triggered, the system automatically checks for existing intake records. If the target folders are missing, it initializes the mock data utility, sweeps the intake directory, and streams live processing telemetry directly into the standard output:Plaintext=== STARTING ENTERPRISE DATA INTAKE PIPELINE ===
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
Final Data Compilation OutputOnce the pipeline exits cleanly, it compiles all analyzed profiles, structures them using Pandas, and outputs a standardized, production-ready dataset named unified_corporate_database.csv containing the following enforced column matrix:sender_nameorganizationcontact_channelintentfinancial_valueprioritysource_fileRobert ChenChen ManufacturingPhoneSales Lead12000Highcall_audio_trans_44102.logsuper_skater99...IndividualEmailRefund Request49Highincoming_msg_99.txtAmanda RossIndividualWebFormFeedback0Lowweb_form_dump_alpha.data🔒 Security & Data GovernanceThis repository implements strict data governance practices:Credential Isolation: No plain-text passwords or API tokens are hardcoded into the architecture. Authentication is performed natively via environment memory variables (os.environ).Git Boundary Shields: The configuration layer uses a .gitignore blueprint to actively block local development assets (.venv/), transient caches (__pycache__/), unstructured source logs (raw_data_intake/), and generated sheets (.csv) from ever leaking onto the public internet.
