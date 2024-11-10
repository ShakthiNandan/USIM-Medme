
function openEditModal(patientId) {
    document.getElementById('editModal').style.display = 'block';
    document.getElementById('editForm').action = '/edit/' + patientId;
}

function closeEditModal() {
    document.getElementById('editModal').style.display = 'none';
}

function confirmDischarge(patientId) {
    if (confirm("Are you sure you want to discharge this patient?")) {
        fetch('/discharge/' + patientId, { method: 'POST' })
            .then(() => location.reload());
    }
}
