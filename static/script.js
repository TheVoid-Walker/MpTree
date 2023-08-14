document.getElementById('modify_link').addEventListener('click', function() {
    var youtubeLink = document.getElementById('youtube_link').value;
    
    // Check if the link already contains "ssyoutube"
    if (!youtubeLink.includes("ssyoutube.com")) {
        var modifiedLink = youtubeLink.replace("youtube.com", "ssyoutube.com");
        document.getElementById('youtube_link').value = modifiedLink;
    }
});
