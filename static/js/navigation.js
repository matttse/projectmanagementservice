var htmlOutput = "";
/**
 * Main function build page
 * Usage: on ready
 */
$(function() {
    $('#body').html('loading...');

    render();

});

function detectRedirect() {
    var url = window.location.hash.toString();
    var section = url.split('#')[1];
    var redirect = true;

    // Case statement to redirect to appropriate pages
    switch (section) {
        case "issues":
            loadIssues();
            
            break;
        case "project_requirements":            
            loadProjectTracking();
            
            break;
        case "chat":
            loadChat();
            break;
        default:
            // statements_def
            $('.pageContent').load('static/html/home.html')
            redirect = false;
            break;
    }

    return redirect;

}


function generateDivContainers() {
    htmlOutput += '<div id="navigation"></div>';
    htmlOutput += '<div class="pageContent"></div>';
}

function importScripts() {

    htmlOutput +=
        '<!-- Popper.js, then Bootstrap JS -->' +
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>' +
        '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>' +
        '<!-- Material Design JS -->' +
        '<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.5.7/js/mdb.min.js"></script>';
}


function render() {
    //navbar and page cont containers
    generateDivContainers();
    //navbar scripts
    importScripts();

    //load main contents
    $('.body').html(htmlOutput);

    //load page into navbar container
    $('#navigation').load('static/html/navbar.html');

    //check url anchors
    detectRedirect(function(redirect) {
        console.log('Redirect')
        redirect ? location.reload(true) : location.reload(false);
    });

    // Try to reload page if accessing from back button
    if (performance.navigation.type == 2) {
        console.log('History navigation, reloading page');
        location.reload(true);
    }
}

function loadDashboard() {
    $('.pageContent').load('static/html/dashboard.html');

}

function loadIssues() {
    $('.pageContent').load('static/html/issues.html');

}

function loadChat() {
    $('.pageContent').load('static/html/chat.html');

}

function loadProjectTracking() {
    $('.pageContent').load('static/html/project_requirements.html');

}
