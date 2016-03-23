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

//for company-profile tabs
$(document).ready(function(){
    $("#myTab a").click(function(e){
    	e.preventDefault();
    	$(this).tab('show');
    });
});

//update company description
$(function(){
    $('#update').click(function () {
        var mysave = $('#desc-content').html();
        $('#hiddeninput').val(mysave);
    });
});

//when decription has focus
function isFocused() {
  if (document.activeElement.id == "desc-content") {
         $('#update').css({
           'visibility' :'visible'
        });
    }
}

//when loses focus
//$(function() {
//  $('#desc-content').focusout(function() {
//    $('#update').css({
//        'visibility' : 'hidden'
//    });
//  });
//})


//edit button occurs when list item is focused out

//$(".block").mouseover(function() { $('#edit').css({
//           'visibility' :'visible'
//        }); })
//        .mouseout(function() { $('#edit').css({
//           'visibility' :'hidden'
//        }); }, 500); })
//        });