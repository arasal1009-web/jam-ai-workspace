# Weekly Tool Scout Report — 2026-09-05

## Focus this week

**Focus area:** privacy-first **BBX + Atlas call/meeting evidence pipeline**.

**Why this focus:** recent handoffs show BBX depends on Jude’s PC-local call recordings/transcripts, while Atlas needs cleaner meeting-to-action and evidence organization. This week’s shortlist prioritizes local/open-source transcription, speaker diarization, word timestamps, and scriptable exports that agents can turn into BBX call logs, CRM update queues, Atlas task summaries, and handoff notes without uploading private audio by default.

**Boundary followed:** no packages/apps/models were installed, no accounts were created, no audio/private files were uploaded, no integrations were connected, and no workflows were changed as final.

## Top recommendations

| Tool | Free? | AI-operable? | Project fit | Why useful | Risk/approval needed | Suggested safe trial |
|---|---|---|---|---|---|---|
| **faster-whisper** | **Open-source / MIT**. PyPI latest checked: `1.2.1`. | **5/5** — Python library, batchable, file-based outputs, works well in deterministic scripts. | **BBX**, Atlas, JAM Workspace. | Best default building block for Jude’s PC call transcription pipeline: scriptable, faster/lower-memory than standard Whisper per official README, supports CPU/GPU, and PyAV bundles FFmpeg libraries. Agents can process transcript text into call outcomes, follow-up tasks, and CRM queue notes. | Installing/running on Jude’s PC/VPS or downloading models needs approval. GPU setup can be fiddly; private audio should stay local unless Jude approves sync/upload. | **No-install next step:** draft a PC-local transcript-folder spec: `recordings/` → transcript `.txt/.json` → agent summary Markdown → BBX/Atlas handoff. |
| **whisper.cpp** | **Open-source / MIT**. GitHub repo checked and active. | **5/5** — native CLI, C API, local/offline, CPU-first, file-based workflow. | **BBX PC transcription**, low-resource/offline fallback, JAM tools. | Strongest local/offline CLI fallback if Python/GPU dependencies are too heavy. Official README highlights CPU-only inference, offline/on-device use, `whisper-cli`, and C-style API. Good for simple repeatable “transcribe this WAV” scripts. | Building binaries/models on Jude’s PC needs approval. README notes CLI expects 16-bit WAV inputs, so a conversion step may be required. | **No-install next step:** create a comparison checklist for Jude’s existing PC script: speed, accuracy, setup difficulty, output format, and WAV conversion need. |
| **WhisperX** | **Open-source / BSD-2-Clause**. PyPI latest checked: `3.8.6`. | **4/5** — CLI/Python-style pipeline, word timestamps, diarization integration, batch inference. | **Atlas meetings**, BBX longer calls, Story interview/reference audio if any. | Best candidate when transcripts need **speaker-ish structure and word-level timestamps**. Official README describes fast ASR, word-level timestamps, VAD preprocessing, and multispeaker ASR using pyannote diarization. | GPU/CUDA setup is more complex; diarization may require pyannote/Hugging Face model terms or token. Use only local/private-safe mode unless Jude approves hosted/API paths. | **No-install next step:** mark it as the phase-2 upgrade after a faster-whisper/whisper.cpp baseline works. Test later on one non-sensitive sample audio. |
| **pyannote.audio `community-1`** | **Open-source toolkit / MIT repo**; PyPI latest checked: `4.0.7`; pretrained model access may have conditions. | **4/5** — Python API; local diarization pipeline once model access is configured. | **Atlas meeting speaker labels**, BBX calls with multiple speakers. | Useful for “who spoke when” diarization. Official README says `community-1` runs locally and prints speaker turn start/stop labels. This can make Atlas evidence timelines and call summaries easier to audit. | Requires ffmpeg, Python deps, and accepting Hugging Face model user conditions; that may require account/token. Any account/model setup needs Jude approval. Diarization is not identity verification. | **No-install next step:** keep as optional module in a future transcript pipeline design, not first install. |
| **WhisperStreaming / SimulStreaming path** | **Open-source / MIT for WhisperStreaming**; repo itself says WhisperStreaming is becoming outdated and points to SimulStreaming. | **3/5** — scriptable, but mainly for live/streaming use and more moving parts. | Future live Atlas/BBX meeting assistant, not immediate weekly workflow. | Worth watching only if Jude later wants real-time transcription. For now, file-based post-call transcription is safer and simpler. | Live transcription touches active meetings/calls and may create privacy/consent issues. Needs explicit approval, plus clear “recording/transcription consent” practice. | **Defer:** do not trial until the offline post-call transcript pipeline is stable and Jude approves live capture. |

## Best pick this week

**Best pick: faster-whisper as the baseline engine for a PC-local transcript-to-action pipeline.**

Reason: it is free/open-source, scriptable from Python, easier to integrate with Jude’s existing “PC recording → Python transcription script → Claude co-work/Hermes logging” pattern, and does not require sending private BBX/Atlas audio to an external service by default.

A practical future architecture, pending approval before any install/change:

```text
Jude PC call/meeting recording folder
  → local transcription script using faster-whisper or whisper.cpp
  → transcript .txt + structured .json
  → agent-generated Markdown summary
  → BBX call outcome / Atlas action queue draft
  → Jude approval before Notion/Sheets/CRM/AppSheet/email updates
```

## Free/open-source alternatives

- **whisper.cpp** — best offline CLI fallback; useful if Jude wants a simple binary/command rather than Python-heavy tooling.
- **WhisperX** — best phase-2 option for word timestamps and speaker diarization when a baseline transcript already works.
- **pyannote.audio community pipeline** — useful for speaker turns, but adds model-access/setup complexity.
- **Existing repo scripts** — keep deterministic scripts as the first layer: BBX plan generator, Sheet update helpers, Story scanners, and Markdown handoffs should remain the WAT execution pattern.

## Manual-only tools to avoid or defer

- Meeting-note apps that require uploading BBX/Atlas audio before local transcription is tested.
- Closed desktop transcription apps with no CLI/API/export path.
- Browser extensions or meeting bots that join calls automatically; these need consent, account access, and stronger approval gates.
- Real-time transcription stacks before the post-call local transcript workflow is reliable.

## Approval needed from Jude

Jude approval is needed before:

- installing faster-whisper, whisper.cpp, WhisperX, pyannote.audio, FFmpeg, CUDA packages, models, or desktop apps;
- downloading models on the PC/VPS;
- syncing PC recordings/transcripts to VPS/Hermes/GitHub/Drive/Notion;
- uploading private BBX/Atlas recordings to any hosted transcription service;
- connecting Google/Notion/CRM/AppSheet accounts;
- writing transcript-derived updates into Notion, Google Sheets, CRM, AppSheet, email, or messages;
- enabling live transcription, meeting bots, webhooks, cron, or containers.

## Next safe action

**Safest next action with no external writes:** create a one-page **BBX/Atlas PC-local transcript pipeline spec** in Markdown only. It should document:

1. input folder naming;
2. output transcript formats (`.txt`, `.json`, Markdown summary);
3. required metadata fields: date, project, participant names if known, source filename, confidence/uncertainty;
4. BBX call outcome fields and Atlas action/evidence fields;
5. approval gates before any Notion/Sheets/CRM/AppSheet updates.

No install is needed for that planning step.

## Sources checked

- GitHub API metadata checked 2026-09-05 for `ggerganov/whisper.cpp` / redirected `ggml-org/whisper.cpp`, `SYSTRAN/faster-whisper`, `m-bain/whisperX`, `pyannote/pyannote-audio`, and `ufal/whisper_streaming`.
- Official GitHub README/raw sources checked 2026-09-05 for the same projects.
- PyPI JSON checked 2026-09-05 for `faster-whisper`, `whisperx`, and `pyannote.audio`.
