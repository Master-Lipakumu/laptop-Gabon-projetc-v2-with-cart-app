function print(pdf) {
    // Create an IFrame.
    var iframe = document.createElement('iframe');  
    // Hide the IFrame.  
    iframe.style.visibility = "hidden"; 
    // Define the source.  
    iframe.src = pdf;        
    // Add the IFrame to the web page.
    document.body.appendChild(iframe);  
    iframe.contentWindow.focus();       
    iframe.contentWindow.print(); // Print.
}