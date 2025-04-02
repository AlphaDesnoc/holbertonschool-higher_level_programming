document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('btn_translate').addEventListener('click', () => {
        const langCode = document.getElementById('language_code').value;
        fetch(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('hello').textContent = data.hello;
            });
    });
});