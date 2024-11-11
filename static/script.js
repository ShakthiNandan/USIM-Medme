let cycleCounter = 0;
let manualCycleCounter = 0;
let lapCounter = 0;

let assistedCprInterval;
let manualCprInterval;
let intubatedCprInterval;

// Start Assisted CPR Timer
document.getElementById("start-assisted-cpr").addEventListener("click", () => {
    let compressionTimer = 30;
    let breakTimer = 5;

    assistedCprInterval = setInterval(() => {
        // Countdown compression timer
        if (compressionTimer > 0) {
            document.getElementById("compression-timer").textContent = compressionTimer;
            compressionTimer--;
        } else if (breakTimer > 0) {
            // Break Timer countdown
            document.getElementById("compression-timer").textContent = breakTimer;
            breakTimer--;
        } else {
            // Reset break timer after 5 seconds and increment cycle counter
            cycleCounter++;
            document.getElementById("cycle-counter").textContent = cycleCounter;
            compressionTimer = 30; // Reset compression timer
            breakTimer = 5; // Reset break timer
        }
    }, 1000); // 1 second interval
});

// Start Manual CPR Timer
document.getElementById("start-manual-cpr").addEventListener("click", () => {
    let compressionTimer = 30;
    let breakTimer = 5;

    manualCprInterval = setInterval(() => {
        if (compressionTimer > 0) {
            document.getElementById("manual-compression-timer").textContent = compressionTimer;
            compressionTimer--;
        } else if (breakTimer > 0) {
            document.getElementById("manual-compression-timer").textContent = breakTimer;
            breakTimer--;
        } else {
            // Reset after each cycle
            manualCycleCounter++;
            document.getElementById("manual-cycle-counter").textContent = manualCycleCounter;
            compressionTimer = 30; // Reset compression timer
            breakTimer = 5; // Reset break timer
        }
    }, 1000); // 1 second interval
});

// Start Manual Intubated CPR Timer
document.getElementById("start-intubated-cpr").addEventListener("click", () => {
    let intubatedTimer = 120;

    intubatedCprInterval = setInterval(() => {
        if (intubatedTimer > 0) {
            document.getElementById("intubated-timer").textContent = intubatedTimer;
            intubatedTimer--;
        } else {
            lapCounter++;
            document.getElementById("lap-counter").textContent = lapCounter;
            intubatedTimer = 120; // Reset after each lap
        }
    }, 1000); // 1 second interval
});

// Reset all counters
document.getElementById("reset-all").addEventListener("click", () => {
    clearInterval(assistedCprInterval);
    clearInterval(manualCprInterval);
    clearInterval(intubatedCprInterval);

    cycleCounter = 0;
    manualCycleCounter = 0;
    lapCounter = 0;

    document.getElementById("cycle-counter").textContent = cycleCounter;
    document.getElementById("manual-cycle-counter").textContent = manualCycleCounter;
    document.getElementById("lap-counter").textContent = lapCounter;
    document.getElementById("compression-timer").textContent = 30;
    document.getElementById("manual-compression-timer").textContent = 30;
    document.getElementById("manual-break-timer").textContent = 5;
    document.getElementById("intubated-timer").textContent = 120;
});
