# BEHAVIORAL ARCHITECTURE FOR DIGITAL DUTY OF CARE
### A Triple Shield Framework & The Wellbeing Passport Protocol

**SSFLAB Research Vol. 1 | FILIGRANA MAGAZINE — VOL. I**
**27 de Agosto 2026 | Andrés Garbán Hernández**

> El acuerdo de $18 mil millones entre Meta y 52 Fiscales Generales (agosto 2026) no es un final, es el inicio de un nuevo estándar: **Duty of Care by Design.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21461785.svg)](https://doi.org/10.5281/zenodo.21461785)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)
[![Meta Case](https://img.shields.io/badge/Meta-$18B_Settlement-red)](https://github.com/ssfactorylabel/ssflab-meta-triple-shield)

![FILIGRANA VOL I - WHAT MAKES YOUR HEART BEAT?](assets/filigrana-cover.png)

### 📰 ABSTRACT

Este repo operacionaliza el paper **Ssflabs_meta_case_1.pdf**. La orden de $18B deja 3 vacíos: migración cross-platform, alucinación autoritaria de IA, y la ineficacia de una fundación tradicional.

Proponemos **Triple Shield Framework** y 2 artefactos open-source listos para auditar.

---

### 🛡️ TRIPLE SHIELD FRAMEWORK

**Shield 1 — LEGAL: DATA TRUST FIDUCIARIO**
No una fundación que recibe donación. Un Data Trust independiente, dueño legal del schema anonimizado.
Board: 3 padres, 3 académicos, 2 teen reps, 1 auditor externo. Meta cede data en fideicomiso, no dona.

**Shield 2 — SOFTWARE: GRADUATED AUTONOMY ENGINE + USER-CONTROLLED AUTOPLAY**
En vez de `IF age < 18 THEN block_access()` proponemos:
`IF self_regulation_score < threshold THEN require_co-configuration() ELSE grant_autonomy()`
Default OFF para <18. El teen lo activa configurando sus propios límites. Cada elección entrena su autonomía.

**Shield 3 — CYBER: CROSS-PLATFORM WELLBEING PASSPORT**
Solución a la migración. Zero-Knowledge Wellbeing Quota.
JWT anónimo firmado con App Attest / Play Integrity: `{"h": hash_anon, "quota_used": 90, "reset": "2026-08-26T00:00Z"}`
Instagram verifica firma, no sabe qué vio en TikTok.
API: `POST /v1/wellbeing-passport/verify` → 200 OK / 429 Quota Exceeded.

---

### 📦 QUICK START

```bash
npm install
npm run test-passport
python src/protocols/autoplay_protocol.py
🔬 SCIENTIFIC GROUNDING

- Nudge Theory (Thaler & Sunstein)
- Self-Determination Theory (Deci & Ryan) — la autonomía es clave
- Ecological Systems Theory (Bronfenbrenner) — contrato hogar-dispositivo-escuela
- SSFLAB: Algorithmic Truthfulness & Consciousness [10.5281/zenodo.21461785]

---

📊 ACCOUNTABILITY METRICS (para el Data Trust)

No medir "tiempo en pantalla". Medir:
- Algorithmic Honesty Score
- Autonomy Recovery Rate (% teens que configuran sus límites)
- Cross-Platform Migration Rate

---

🗺️ ROADMAP

- *Phase 1 (0-3m):* Open source Autoplay Protocol
- *Phase 2 (3-6m):* Pilot Data Trust con 2 universidades
- *Phase 3 (6-12m):* Wellbeing Passport API como estándar W3C propuesto a Meta, TikTok, YouTube.

*Resultado:* Meta pasa de demandado a autor de estándar de industria. Triple protección: Legal, Cyber, Engineering.

---

📄 PAPER

Full paper en `/docs/Ssflabs_meta_case_1.pdf`

*Citar:*
Garbán Hernández, A. (2026). Behavioral Architecture for Digital Duty of Care: A Triple Shield Framework & The Wellbeing Passport Protocol. SSFLAB Research Vol. 1.

---
