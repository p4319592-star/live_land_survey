# Q-GibberLink — Quantum-Secured AI Agent Communication Platform

## Overview

**Q-GibberLink** is the first quantum-secured communication platform for AI-to-AI data exchange using the GibberLink acoustic protocol. When two AI agents discover they are both AI, they switch from human-readable English to GGWave audio beeps for efficiency. Q-GibberLink secures this acoustic channel with a hybrid **QKD (BB84) + PQC (Kyber768)** protocol and a trust-aware controller that auto-falls back to PQC when the quantum channel is compromised.
Here are both links to access the dashboard:

Network Link (for phone, tablet, or other devices on the same Wi-Fi):

👉 http://192.168.43.253:8501

Direct Link (for this computer):

👉 http://localhost:8501



> **Hackathon Track 1: Quantum Cryptography & Security**

---

## The Problem

AI agents increasingly communicate with each other over networks. The **GibberLink** protocol (popularized at the ElevenLabs hackathon) allows two AIs to discover each other and switch from English to an acoustic modem protocol (GGWave) for bandwidth-efficient data transfer.

However, plain GibberLink has **no encryption** — any microphone can capture the audio beeps and decode the message. As AI-to-AI communication becomes ubiquitous, this is a critical security gap.

Furthermore, future adversaries may have **quantum computers** capable of breaking classical encryption (RSA, ECC). A security solution that is robust against both quantum and classical attacks is needed.

---

## The Innovation

Q-GibberLink introduces **Q-SHIELD** — a hybrid security protocol that combines:

1. **Quantum Key Distribution (BB84)** — information-theoretic security via quantum mechanics. Any eavesdropping on the quantum channel is detected through QBER (Quantum Bit Error Rate) monitoring.

2. **Post-Quantum Cryptography (Kyber768)** — NIST-standardized lattice-based KEM that resists quantum computer attacks.

3. **Trust-Aware Controller** — monitors QBER and channel loss in real time:
   - **QBER < 11% and loss < 60%** → **HYBRID mode**: Final key = SHA3-256(PQC_key XOR SHA3-256(QKD_key))
   - **QBER > 11%** (Eve detected) → **PQC_ONLY mode**: Abandon QKD, use Kyber768 only
   - **Loss > 60%** (channel degraded) → **PQC_ONLY mode**

4. **Attack Marketplace** — three quantum attacks are implemented for security testing:
   - **Intercept-Resend**: Eve measures qubits, introducing ~25% QBER (easily detected)
   - **Photon Number Splitting (PNS)**: Eve splits multi-photon pulses — low QBER but high info leak (stealthy)
   - **Detector Blinding**: Eve controls Bob's detectors — 0% QBER but full key compromise (evades QBER monitoring)

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Q-GibberLink Platform                      │
│                                                               │
│  ┌──────────────┐    ┌──────────────────┐    ┌────────────┐  │
│  │   Alice AI   │    │  Q-SHIELD Hybrid │    │   Bob AI   │  │
│  │              │───▶│   Protocol       │───▶│            │  │
│  │  English     │    │                  │    │  English   │  │
│  │  Detection   │    │  ┌────────────┐  │    │  Detection │  │
│  │  Switch to   │    │  │  BB84 QKD  │  │    │  Switch to │  │
│  │  GibberLink  │    │  │  (Qiskit)  │  │    │  GibberLink│  │
│  │              │    │  └─────┬──────┘  │    │            │  │
│  │  AES-GCM     │    │        │         │    │  AES-GCM   │  │
│  │  Encrypt     │    │  ┌─────▼──────┐  │    │  Decrypt   │  │
│  │  GGWave      │    │  │ Trust      │  │    │  GGWave    │  │
│  │  Audio TX    │    │  │ Controller │  │    │  Audio RX  │  │
│  │              │    │  └─────┬──────┘  │    │            │  │
│  └──────────────┘    │  ┌─────▼──────┐  │    └────────────┘  │
│                      │  │ Kyber768   │  │                     │
│                      │  │ PQC KEM    │  │                     │
│                      │  └─────┬──────┘  │                     │
│                      │        │         │                     │
│                      │   SHA3-256 XOR   │                     │
│                      │   Final Key      │                     │
│                      └──────────────────┘                     │
│                              ▲                                │
│                              │                                │
│                     ┌────────┴────────┐                       │
│                     │  Attack Layer    │                       │
│                     │                  │                       │
│                     │ • Intercept-RS   │                       │
│                     │ • PNS            │                       │
│                     │ • Detector Blind │                       │
│                     └──────────────────┘                       │
│                              ▲                                │
│                     ┌────────┴────────┐                       │
│                     │   Dashboard      │                       │
│                     │  (Streamlit)     │                       │
│                     │                  │                       │
│                     │ • QBER Metrics   │                       │
│                     │ • Plotly Charts  │                       │
│                     │ • Protocol Log   │                       │
│                     │ • Audio Player   │                       │
│                     │ • Key Display    │                       │
│                     └──────────────────┘                       │
└─────────────────────────────────────────────────────────────┘
```

---

## Folder Structure

```
quantum_safety/
├── requirements.txt              # Python dependencies
├── main.py                       # Entry point — launches Streamlit dashboard
├── README.md                     # This file
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── quantum_sim.py            # BB84 simulator using Qiskit AerSimulator
│   └── qber_analyzer.py          # QBER calculation, secure key rate, abort logic
├── protocols/
│   ├── __init__.py
│   ├── bb84.py                   # Pure BB84 key generation
│   ├── e91.py                    # E91 entanglement-based protocol
│   └── qshield_hybrid.py         # CORE INNOVATION: Kyber + QKD hybrid with trust controller
├── attacks/
│   ├── __init__.py
│   ├── base.py                   # Base attack class with common interface
│   ├── intercept_resend.py       # Intercept-Resend attack (QBER 25-35%)
│   ├── pns_attack.py             # Photon Number Splitting (low QBER, high leak)
│   └── detector_blinding.py      # Detector Blinding (0% QBER, full compromise)
├── ai_agents/
│   ├── __init__.py
│   ├── gibberlink_audio.py       # GGWave audio encode/decode + AES-GCM quantum-secure layer
│   └── agent_comm.py             # Alice AI <-> Bob AI negotiation simulation
├── dashboard/
│   ├── __init__.py
│   └── app.py                    # Streamlit professional dashboard
└── tests/
    ├── __init__.py
    └── test_qber.py              # Unit tests for QBER, BB84, attacks, Q-SHIELD
```

---

## Installation & Running

### Prerequisites

- Python 3.9+
- pip

### Install Dependencies

```bash
cd quantum_safety
pip install -r requirements.txt
```

### Run the Dashboard

```bash
python main.py
```

This launches the Streamlit dashboard on **http://localhost:8501**.

### Run Tests

```bash
python -m pytest tests/test_qber.py -v
```

Or without pytest:

```bash
python tests/test_qber.py
```

### Run Individual Modules

Each module includes a standalone demo:

```bash
python core/quantum_sim.py       # BB84 simulation demo
python core/qber_analyzer.py     # QBER analysis demo
python protocols/bb84.py         # BB84 protocol demo
python protocols/e91.py          # E91 protocol demo
python protocols/qshield_hybrid.py  # Q-SHIELD hybrid demo
python attacks/intercept_resend.py  # Intercept-Resend demo
python attacks/pns_attack.py     # PNS attack demo
python attacks/detector_blinding.py  # Detector Blinding demo
python ai_agents/gibberlink_audio.py  # GibberLink audio demo
python ai_agents/agent_comm.py   # AI agent negotiation demo
```

---

## Dashboard Features

### Sidebar Controls

| Control | Options |
|---------|---------|
| Protocol | BB84, Q-SHIELD Hybrid |
| Attack | None, Intercept-Resend, PNS, Detector Blinding |
| Qubits | 50–500 (slider) |
| Eve Intercept Rate | 0–100% (slider) |
| Channel Loss | 0–100% (slider) |
| Launch Button | Executes the simulation |

### Main Dashboard

- **Top Row**: 4 metric cards — QBER %, Secure Key Rate, Eve's Information, Protocol Mode
- **Middle**: Plotly graphs — QBER vs Distance (with 11% abort threshold line), Attack Comparison bar chart
- **Bottom Left**: Protocol Log — real-time trust controller decisions, fallback events, warnings
- **Bottom Right**: GibberLink Audio Player — play the encoded audio, plus Eve's Decoded Attempt (gibberish when secure, plaintext when insecure)
- **Footer**: Final Key display (partial hex), Secure/Insecure badge, AI Agent negotiation status

---

## Key Technical Details

### BB84 Simulation

- Uses **Qiskit AerSimulator** with real quantum circuits
- Each qubit: `X` gate for bit=1, `H` gate for X-basis, `measure` for readout
- Falls back to a mathematical model if Qiskit is not installed
- Batched simulation (50 qubits per batch) for memory efficiency

### QBER Analysis

- QBER = (errors / matched_basis_bits) × 100
- Secure key rate: K = q × [1 - 2×H₂(Q)] (binary entropy formula)
- Abort threshold: QBER > 11% (Shor-Preskill bound)
- Channel loss threshold: > 60%

### Q-SHIELD Hybrid Protocol

- **HYBRID mode**: Final key = SHA3-256(PQC_key XOR SHA3-256(QKD_key))
  - An attacker must break BOTH Kyber768 AND BB84 to recover the key
  - Defense-in-depth: quantum + post-quantum security
- **PQC_ONLY mode**: Final key = SHA3-256(Kyber768 shared secret)
  - Used when QBER > 11% or channel loss > 60%
  - Still secure (Kyber768 is NIST-standardized)
- Uses `kyber-py` library; falls back to `os.urandom(32)` if not installed

### Attack Models

| Attack | QBER | Eve Info | Detection |
|--------|------|----------|-----------|
| Intercept-Resend | 25–35% | ~25% | QBER monitoring ✓ |
| PNS | ~2% | ~5–10% | Needs decoy states |
| Detector Blinding | 0% | 100% | Needs hardware checks |

### GibberLink Audio

- Uses **GGWave** library for acoustic data encoding (FSK beeps)
- AES-GCM encryption (via pycryptodome) before audio encoding
- Falls back to simulated tones if GGWave not installed
- Eve's decode shows gibberish when encrypted, plaintext when not

---

## Demo Video Script

1. **Introduction** (30s): "Q-GibberLink secures AI-to-AI communication with quantum cryptography..."

2. **Clean Channel Demo** (2s to 60s):
   - Select Protocol: Q-SHIELD Hybrid, Attack: None
   - Launch → Show HYBRID mode, low QBER, secure key
   - Play the GibberLink audio beep
   - Show Eve's decode: "gibberish" (encrypted)

3. **Intercept-Resend Attack** (60s):
   - Select Attack: Intercept-Resend, Eve rate: 100%
   - Launch → QBER jumps to ~25%, above 11% threshold
   - Trust controller: "ABORT QKD → PQC_ONLY"
   - Key still secure (PQC), but warning shown
   - Protocol log shows fallback decision

4. **PNS Attack** (45s):
   - Select Attack: PNS
   - Launch → QBER stays low (~2%), but Eve info is high
   - Explain: "PNS evades QBER monitoring — needs decoy states"

5. **Detector Blinding** (45s):
   - Select Attack: Detector Blinding
   - Launch → QBER = 0%, but Eve info = 100%
   - Show INSECURE badge — "0% QBER doesn't mean secure!"

6. **Q-SHIELD Hybrid Advantage** (30s):
   - Compare BB84 vs Q-SHIELD under attack
   - BB84 fails → Q-SHIELD falls back to PQC → still secure

7. **Conclusion** (15s): "First quantum-secured GibberLink — hybrid QKD + PQC for the post-quantum AI era."

---

## Dependencies

| Package | Purpose |
|---------|---------|
| qiskit | Quantum circuit framework |
| qiskit-aer | Quantum circuit simulator (AerSimulator) |
| numpy | Numerical operations |
| matplotlib | Plotting (fallback) |
| streamlit | Dashboard web framework |
| plotly | Interactive charts |
| ggwave | Acoustic modem protocol |
| kyber-py | Post-quantum KEM (Kyber768) |
| pycryptodome | AES-GCM encryption |

> **Note**: If optional libraries (qiskit, ggwave, kyber-py, pycryptodome) are not installed, the platform gracefully falls back to placeholder implementations and remains fully functional for demonstration.

---

## License

MIT License — Built for hackathon demonstration purposes.

## Team

IRON_LAB Research Team — Hackathon Track 1: Quantum Cryptography & Security
