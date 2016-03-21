$(function() {	
    $( "#id_startDate" ).datepicker({
    	showAnim: 'slideDown',
    	numberOfMonths:1,
    	// dateFormat: 'dd-mm-yy',
    	minDate: 0,
    	onclose: function( selectedDate ){
    		$("#id_endDate").datepicker("option", "minDate", selectedDate);
    	}

    });
  
	
    $( "#id_endDate" ).datepicker({
    	showAnim: 'slideDown',
    	numberOfMonths:1,
    	// dateFormat: 'dd-mm-yy',
    	onclose: function( selectedDate ){
    		$("#id_startDate").datepicker("option", "maxDate", selectedDate);
    	}
    });
  });


$(document).ready(function() {
	$(".project-desc-text").dotdotdot();
});

