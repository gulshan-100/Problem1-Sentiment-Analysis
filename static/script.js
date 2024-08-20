document.getElementById('uploadButton').addEventListener('click', () => {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if (!file) {
        alert('Please select a file.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const resultContainer = document.getElementById('resultContainer');
        resultContainer.innerHTML = ''; // Clear previous results

        if (data.error) {
            resultContainer.innerHTML = `<p style="color: red;">${data.error}</p>`;
        } else {
            data.results.forEach(result => {
                const resultItem = document.createElement('div');
                resultItem.classList.add('result-item');

                resultItem.innerHTML = `
                    <h3>Text: ${result.text}</h3>
                    <p><strong>Sentiment:</strong> ${result.sentiment} (Confidence: ${result.confidence.toFixed(2)})</p>
                    <p><strong>Timestamp:</strong> ${result.start} - ${result.end}</p>
                `;
                resultContainer.appendChild(resultItem);
            });
        }
    })
    .catch(error => {
        document.getElementById('resultContainer').innerHTML = `<p style="color: red;">An error occurred: ${error.message}</p>`;
    });
});
