$('.input-table').attr('disabled', true);
$('.select').attr('disabled', true);
$('.input-value-tab').attr('disabled', true);
$('textarea[name="total_mission"]').closest('.value-table-score').addClass('box-required');
$('textarea[name="total_mission"]').change(function(){
	$('textarea[name="total_mission"]').closest('.value-table-score').removeClass('box-required');
	if (!$('select[name="start_YYYYMM"]').attr("disabled")) return;
  $('select[name="start_YYYYMM"]').addClass('box-required');  
  $('select[name="start_YYYYMM"]').removeAttr("disabled");
});
$('select[name="start_YYYYMM"]').change(function(){
  $('select[name="start_YYYYMM"]').removeClass('box-required');
  if (!$('select[name="end_YYYYMM"]').attr("disabled")) return;
  $('select[name="end_YYYYMM"]').removeAttr("disabled");
  $('select[name="end_YYYYMM"]').addClass('box-required');
});
$('select[name="end_YYYYMM"]').change(function(){
  $('select[name="end_YYYYMM"]').removeClass('box-required');
  if (!$('input[name="A_keyword"]').attr("disabled")) return;
  $('input[name="A_keyword"]').removeAttr("disabled");
  $('input[name="A_keyword"]').addClass('box-required');
  $('textarea[name="A_dueto"]').removeAttr("disabled");
});
var key_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
for (let i = 0; i < key_array.length; i++) {
	$(`input[name="${key_array[i]}_keyword"]`).change(function(){
		$(`input[name="${key_array[i]}_keyword"]`).removeClass('box-required');
		if (i < key_array.length - 1) {
			if (!$(`input[name="${key_array[i + 1]}_keyword"]`).attr("disabled")) return;
		  $(`input[name="${key_array[i + 1]}_keyword"]`).removeAttr("disabled");
		  $(`input[name="${key_array[i + 1]}_keyword"]`).addClass('box-required');
		  $(`textarea[name="${key_array[i + 1]}_dueto"]`).removeAttr("disabled");
		} else {
			if (!$(`textarea[name="${key_array[0]}1_content"]`).attr("disabled")) return;
		  $(`textarea[name="${key_array[0]}1_content"]`).removeAttr("disabled");
		  $(`textarea[name="${key_array[0]}1_content"]`).closest('.value-table').addClass('box-required');
		}
	});		
	for (let j = 1; j < 9; j++) {
		$(`textarea[name="${key_array[i]}${j}_content"]`).change(function(){
			$(`textarea[name="${key_array[i]}${j}_content"]`).closest('.value-table').removeClass("box-required");
			if(j < 8) {
				if (!$(`textarea[name="${key_array[i]}${j + 1}_content"]`).attr("disabled")) return;
			  $(`textarea[name="${key_array[i]}${j + 1}_content"]`).removeAttr("disabled");			
				$(`textarea[name="${key_array[i]}${j + 1}_content"]`).closest('.value-table').addClass("box-required");
			}
		  if(j == 8 && i < key_array.length - 1) {
		  	if (!$(`textarea[name="${key_array[i + 1]}1_content"]`).attr("disabled")) return;
			  $(`textarea[name="${key_array[i + 1]}1_content"]`).removeAttr("disabled");		  	
				$(`textarea[name="${key_array[i + 1]}1_content"]`).closest('.value-table').addClass("box-required");
		  }
		});
	}
}