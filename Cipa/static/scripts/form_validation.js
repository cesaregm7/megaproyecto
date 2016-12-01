

function validateForm() {
    var number_elements = $('input:number');
    for (var i=0;i<number_elements.length;i++){
        if(isNaN(number_elements[i].value)){
	    alert('Revise campos numericos');
	    return false;
	}
        if(number_elements[i].value==""){
	    alert('Revise campos numericos');
	    return false;
	}
    }
    var date_elements = $('input[type=date]');
    for (var i=0;i<date_elements.length;i++){
        if(date_elements[i].value == ""){
            alert('Revise campos fechas');
	    return false;
	}
    }
    return true;
}

