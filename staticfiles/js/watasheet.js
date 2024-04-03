function func_count_type(element){
    let group = $(element).data('group');
    if ($(element).is(":checked")) {
    	typeList[group] += 1;
    } else {
    	typeList[group] -= 1;
    }
    for (var type in typeList) {
        if (typeList.hasOwnProperty(type)) {
           $(`#type_${type}`).text(typeList[type]);
        }
    }
}

