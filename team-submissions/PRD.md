Prithvinesan Thanigainesan (Prithvi)
discord: laidfiaisd
email: prithvi005040@gmail.com
github: prithvi-thanigainesan
### Final Optimization Result
- **Sequence Length (N):** 40
- **Energy (E):** 108.0
- **Merit Factor (F):** 7.4074
- **Optimal Sequence:** [-1. -1.  1.  1. -1. -1. -1.  1. -1. -1.  1. -1. -1. -1. -1.  1. -1.  1.
 -1. -1.  1.  1.  1. -1.  1. -1.  1.  1.  1. -1.  1. -1. -1. -1. -1. -1.
  1.  1.  1.  1.]
        
If I had more time, I could've probably gotten a better result with better energy and a merit factor. But I am happy with what I achieved in the given time. Thank you, guys, for the opportunity, and have a great day!

tests.py is the verification script.
video.mov is my presentation.

# Product Requirements Document (PRD)

**Project Name:** [LABSsoln]
**Team Name:** [Unitary Evolution]
**GitHub Repository:** [Insert Link Here]

---

> **Note to Students:** > The questions and examples provided in the specific sections below are **prompts to guide your thinking**, not a rigid checklist. 
> * **Adaptability:** If a specific question doesn't fit your strategy, you may skip or adapt it.
> * **Depth:** You are encouraged to go beyond these examples. If there are other critical technical details relevant to your specific approach, please include them.
> * **Goal:** The objective is to convince the reader that you have a solid plan, not just to fill in boxes.

---

## 1. Team Roles & Responsibilities [You can DM the judges this information instead of including it in the repository]

| Role | Name | GitHub Handle | Discord Handle
| :--- | :--- | :--- | :--- |
| **Project Lead** (Architect) | [Prithvinesan Thanigainesan] | [@prithvi-thanigainesan] | [@laidfiaisd] |
| **GPU Acceleration PIC** (Builder) | [Prithvinesan Thanigainesan] | [@prithvi-thanigainesan] | [@laidfiaisd] |
| **Quality Assurance PIC** (Verifier) | [Prithvinesan Thanigainesan] | [@prithvi-thanigainesan] | [@laidfiaisd] |
| **Technical Marketing PIC** (Storyteller) | [Prithvinesan Thanigainesan] | [@prithvi-thanigainesan] | [@laidfiaisd] |

---

## 2. The Architecture
**Owner:** Prithvinesan Thanigainesan

### Choice of Quantum Algorithm
* **Algorithm:** [Warm Started Quantum Approximation Algorithm (WS QAOA) with a ZY rotation Ansatz]

* **Motivation:** [In my Phase 1 trials, I noticedthat standard quantum approaches often wander into high energy states that have nothing to do with the actual LABS structure. I chose Warm Started QAOA because I wanted to give our quantum circuit a head start using a classical approximation. Instead of total randomness, I'm pointing the algorithm in the direction of the first gate. I also decided to implement a symmetry preserving mixer. The LABS problem has great math, like the fact that flipping all the bits doesn't change energy. I didn't want my algorithm wasting time exploring soltuions that violate these basic symmetries. By getting deep into the physics of the problem directly into my gates, I'm making sure every second of GPU time is spent searching for the actual global optimum, not just the noise.]


### Literature Review
* **Reference:** [Egger, D. J., et al. (2021). "Warm-starting quantum optimization., Daniel J. Egger1, Jakub Mareček2, and Stefan Woerner1, https://quantum-journal.org/papers/q-2021-06-17-479/pdf/]
* **Relevance:** [This is my primary roadmap. Egger proved that if you start a quantum optimizer near a good classical guess, you can get away with much shallower circuits. For me, shallower circuits mean faster simulations on the L4 GPU and a much higher chance of finding that perfect N = 40 sequence before I run out of credits]
* 
---

## 3. The Acceleration Strategy
**Owner:** Prithvinesan Thanigainesan

### Quantum Acceleration (CUDA-Q)
* **Strategy:** [I am moving my simulation from the CPU to the 'nvidia cuStateVec' backend]
 
### Classical Acceleration (MTS)
* **Strategy:** [I am replacing the serial one at a time neighbor evaluation with a vectorized delta energy kernel using CuPy]

### Hardware Targets
* **Dev Environment:** [Qbraid (CPU) for initial logic, Brev L4 for my integration part.]
* **Production Environment:** [Brev A100-80GB for final N=50 benchmarks]

---

## 4. The Verification Plan
**Owner:** Prithvinesan Thanigainesan

### Unit Testing Strategy
* **Framework:** [pytest integrated with cupy testing for GPU specific submission]
* **AI Hallucination Guardrails:** [Since I am using an AI collaborative workflowm, I am implementing dual kernel cross check. For every GPU kernel generated, I will maintail a slow golden NumPy reference version on the CPU. My test suite will generate random bitstrings and maintain that the GPU output matches the CPU refernece to within a 10^-5 tolerene. This makes sures that any clever indecing optimizations suggested by the AI haven't made silent math errors]

### Core Correctness Checks
* **Check 1 (Symmetry):** [The LABS problem has three physical symmetries, that is inversionm reversal and complementary reversal  My verification script will pass a sequence through all three transformations and claim that the GPU energy kernel returns the exact same value for all four variations. If these don't match, it means my CuPy indexing has a mistake]
* **Check 2 (Ground Truth):** [for the LABS problem, the energy is theoretically bounded by the sequence length. I will implement a sanity gaurd in my testing script that raises a flag if any quantum seeded result returns an energy value that is physically impossible ]

---

## 5. Execution Strategy & Success Metrics
**Owner:** Prithvinesan Thanigainesan

### Agentic Workflow
* **Plan:** [All architectural desig and lodic refactoring are done on free CPU tiers. Brev GPU instances are for high performance excecution only, launched through CLI to run pre prepared scripts and shut down immediately after data collection is over.]

### Success Metrics
* **Metric 1 (Approximation):** [Metric factor > 8.0 for upto N = 40]
* **Metric 2 (Speedup):** [hit 25x - 50x speedup on MTS neighborhood search compared to CPU baseline]
* **Metric 3 (Scale):** [Succesfully complete N = 60 optimization run within the 20$ budget]

### Visualization Plan
* **Plot 1:** [Comparing the total excecution time of the standard CPU based MTS against the GPU accelerated CuPy implementation.]
* **Plot 2:** [Quantum seeeding success rate (energy congervence vs iterations]

---

## 6. Resource Management Plan
**Owner:** Prithvinesan Thanigainesan

* **Plan:** [To maximize the 20$ budget, I am going with a strategy where all architectural design and core python logic is finalized locally before going to the GPU. I will utilize a cheap Nvidia L4 instance for the primary portinf and debugging, and reserve the A100 for the final 3 - 4 hours of high N benchmarks to leverage its massive memory bandwidth. I am personally responsible for shutting down the instance whenever I go to a meal break or ensure the instance is never idling when I am not actively running code.]

