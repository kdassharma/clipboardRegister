function printClipboard() {

    
    ['cut', 'copy', 'paste'].forEach(function(event) {
        document.addEventListener(event, function(e) {
            console.log(event);  
            console.log(document.execCommand('paste')); 
        });
    });
    
}

function noob() {
    console.log("Hello");
}