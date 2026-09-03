# HydroSambar 🍲
> **Department of Mess Food Dilution & Photometric Sambar Auditing**  
> Built for the TinkerHub Useless Projects make-a-thon.

---

### The Problem
Every engineering student in an Indian hostel has encountered "sambar" that is legally identical to hot tap water with yellow food coloring and seasonal sadness. Finding a solitary piece of drumstick (*muringakka*) in a mess bowl is rarer than a Halley's comet sighting.

**HydroSambar** brings mathematical accountability to the mess committee by utilizing optical spectrometry and computer vision to evaluate sambar quality in real time.

---

### Key Features

* 📱 **Mobile & Laptop Responsive**:
  * Seamlessly switches between the **rear environment camera** (to point directly into a food bowl on your smartphone) and the **front selfie camera**.
  * On laptops, works directly with any built-in or USB webcam.
* 🧪 **Fail-Safe Stage Presets**:
  * Includes built-in simulated calibration samples (*Hostel Mess Yellow Water*, *The Drumstick Miracle*, *Municipal Tap Water*) so you never have to carry an actual bowl of hot soup onto the presentation stage.
* 🔬 **Photometric Metrics Calculated**:
  * **Photometric Transparency**: Measures light penetration through the broth (98.4% = Tap water equivalent).
  * **Vegetable Biomass Count**: Scans for floating solid entities (drumsticks, potatoes, carrots).
  * **Dynamic Viscosity (cP)**: Compared against the baseline viscosity of municipal tap water (1.00 cP).
  * **Warden Guilt Index**: Quantifies the ethical violation committed by the mess contractor.
* 📜 **Official Certificate of Culinary Fraud**:
  * Generates an official, shareable departmental certificate declaring the sambar legally classified as *"Warm Seasoned Shower Water"*.
* 🔊 **Synthesized Voice Verdict**:
  * Uses the browser Speech Synthesis API to deadpan announce the failure to the audience.

---

### How to Run Locally

Open `index.html` in any modern desktop or mobile browser (Chrome, Safari, Edge, Firefox).

```bash
# Optional: serve with a local static server
npx serve .
# or
python -m http.server 8000
```

---

### Stage Presentation Hotkeys
* **`[SPACEBAR]`**: Instant liquid audit trigger.
* **`[C]`**: Switch camera lens (rear/front).
