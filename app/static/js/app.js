document.onkeypress = checkKey;
document.onkeydown = checkKey;

function checkKey (e) {
    e = e || window.event;

    if (e.keyCode === 40) { //arrowDown

    }
    if (e.keyCode === 38) { //arrowUp

    }
    if (e.keyCode === 39) { //arrowRight
        if (!tabFocused(document.activeElement.id)) {
            console.log("set focus to hls");
            document.getElementById("hls").focus();
        } else if (document.activeElement.id === "hls") {
            document.getElementById("smoothstreaming").focus();
        } else if (document.activeElement.id === "smoothstreaming") {
            document.getElementById("dash").focus();
        } else if (document.activeElement.id === "dash") {
            document.getElementById("transportstream").focus();
        } else if (document.activeElement.id === "transportstream") {
            document.getElementById("drm").focus();
        } else if (document.activeElement.id === "drm") {
            document.getElementById("hls").focus();
        }
    }
    if (e.keyCode === 37) { //arrowLeft
        if (!tabFocused(document.activeElement.id)) {
            document.getElementById("hls").focus();
        } else if (document.activeElement.id === "hls") {
            document.getElementById("drm").focus();
        } else if (document.activeElement.id === "drm") {
            document.getElementById("transportstream").focus();
        } else if (document.activeElement.id === "transportstream") {
            document.getElementById("dash").focus();
        } else if (document.activeElement.id === "dash") {
            document.getElementById("smoothstreaming").focus();
        } else if (document.activeElement.id === "smoothstreaming") {
            document.getElementById("hls").focus();
        }
    }
};

function tabFocused(id) {
    let ret = false;
    switch (id) {
        case "hls":
        case "smoothstreaming":
        case "dash":
        case "transportstream":
        case "drm":
            ret = true;
            break;
        default:
            break;
    }
    return ret;
}