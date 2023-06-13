function validateForm() {
    var urlInput = document.getElementById('url');
    var urlValue = urlInput.value.trim();
    
    if (urlValue === '') {
        alert('Please enter a valid YouTube video link.');
        urlInput.focus();
        return false;
    }

    var youtubeRegex = /^(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})$/;
    
    if (!youtubeRegex.test(urlValue)) {
        alert('Invalid YouTube video link.');
        urlInput.focus();
        return false;
    }
    return true;
}

function clearUrlInput() {
    document.getElementById('url').value = '';
}