// active.js

$(document).ready(function(){

	$(window).on('hashchange', function() {

  		$('li').removeClass('active');
  		$('li a').each(function() {
	        if ($(this).prop('id') == location.hash.substr(1,)) {
	            $(this).closest('li').addClass('active');
        	}
	    });
	});
    
});