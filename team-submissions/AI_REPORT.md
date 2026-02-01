> **Note to Students:** > The questions and examples provided in the specific sections below are **prompts to guide your thinking**, not a rigid checklist. 
> * **Adaptability:** If a specific question doesn't fit your strategy, you may skip or adapt it.
> * **Depth:** You are encouraged to go beyond these examples. If there are other critical technical details relevant to your specific approach, please include them.
> * **Goal:** The objective is to convince the reader that you have employed AI agents in a thoughtful way.

**Required Sections:**

1. **The Workflow:** I used clause as the implementation agent to handle the low level CuPy syntax where I defined the mathematical strats.
2. **Verification Strategy:** Since I was vibe coding to generate CuPy kernels, I treated the AI generated code as a  draft that required  physical and mathematical confirmation. I implemented a dedicated test suite that cross referenced the GPU energy outputs against a known N=4 baseline (E=4) to ensure the fundamental logic was good. Also, I enforced a physical correctness check to verify that the energy calculations stayed consistent under sequence inversion (E(S)=E(−S)), which successfully identified and allowed me to fix a hallucinated slicing error in the batch evaluation logic. By manually verifying these drafts before running the full 200 seed search, I guaranteed that the high tier merit factor results were the product of accurate math rather than luck. 


3. **The "Vibe" Log:**
* *Win:* The biggest win was using the AI to rapidly execute my idea for batch neighbor evaluation. Instead of writing the CUDA kernels by hand, I made the agent to vectorize the energy calculation using cupy. This let me to evaluate 40 neighbors for 200 different seeds simultaneously. What would have taken hours to debug manually was implemented in minutes, allowing me to concentrate on the search results.
* *Learn:* During the search, I realized that simply letting the AI optimize for longer runtimes didn't help. The search kept delaying at the same energy points. I had to change how I was prompting the agent, moving away from asking for more iterations and instead asking it to help me restructure the engine for multi start diversity. This change finally broke the delay and reached 108.0.
* *Fail:* While generating the batched energy function, the AI was initially hallucinating a cp.sum operation that lacked the axis=1 parameter. This made the energies of all my parallel seeds to collapse into a single sum. I caught this immediately during a verification go through because the energy values looked really high. I manually corrected the axis alignment to ensure each agent was being tracked independently.
* *Context Dump:* I treated the AI as an execution tool for my decisions. My primary prompt for the final engine was:

"We are hitting a limit at 116.0. I need to pivot. Rewrite the Tabu Search to handle 200 random seeds in parallel. Use CuPy to flip every bit of the current sequence at once for all seeds, calculate the energy of all neighbors in one batch call, and use a penalty mask. I am driving the search, you provide the CUDA optimized syntax."


