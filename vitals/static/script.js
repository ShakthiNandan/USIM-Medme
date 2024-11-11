// Toggle the visibility of the vitals dropdown menu
function toggleVitalsMenu() {
    const dropdown = document.getElementById("vitals-dropdown");
    dropdown.style.display = dropdown.style.display === "none" || dropdown.style.display === "" ? "block" : "none";
}

// Save the vital sign data
function saveVital() {
    const type = document.getElementById("form-title").textContent.toLowerCase().replace(" ", "_");
    const value1 = document.getElementById("systolic")?.value || 0;
    const value2 = document.getElementById("diastolic")?.value || 0;
    
    fetch('/save_vital', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ type, value1, value2 }),
    })
    .then(response => response.json())
    .then(data => {
        alert("Vital sign saved successfully!");
    });
}

// Select a vital sign and update the form content
function selectVital(type) {
    const title = type.replace("_", " ").replace(/\b\w/g, char => char.toUpperCase());
    document.getElementById("form-title").textContent = title;
    
    // Toggle specific form elements based on type
    const bpForm = document.getElementById("bp-form");
    bpForm.style.display = type === "blood_pressure" ? "block" : "none";
    
    // Close the vitals dropdown after selecting
    toggleVitalsMenu();
}
