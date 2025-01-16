document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/statistics')
        .then(response => response.json())
        .then(data => {
            const statsContainer = document.getElementById('stats-container');
            statsContainer.innerHTML = `
                <p>Total circRNAs: ${data.total_circRNAs}</p>
                <p>Total Diseases: ${data.total_diseases}</p>
                <p>Total Functions: ${data.total_functions}</p>
            `;
        });
});
