var modal = document.getElementById("delete-confirmation-modal");

var btn = document.getElementById("delete-button");

var div = document.getElementById("close-button");

btn.onclick = function() {
    modal.style.display = "block";
}

div.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}