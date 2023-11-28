$('.input-table').attr('disabled', true);
$('.select').attr('disabled', true);
$('.input-value-tab').attr('disabled', true);
$('textarea[name="total_mission"]').change(function(){
  $('select[name="start_YYYYMM"]').removeAttr("disabled");
});
$('select[name="start_YYYYMM"]').change(function(){
  $('select[name="end_YYYYMM"]').removeAttr("disabled");
});
$('select[name="end_YYYYMM"]').change(function(){
  $('input[name="A_keyword"]').removeAttr("disabled");
  $('textarea[name="A_dueto"]').removeAttr("disabled");
});
var key_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
for (let i = 0; i < key_array.length; i++) {
	if (i < key_array.length - 1) {
		$(`input[name="${key_array[i]}_keyword"]`).change(function(){
		  $(`input[name="${key_array[i + 1]}_keyword"]`).removeAttr("disabled");
		  $(`textarea[name="${key_array[i + 1]}_dueto"]`).removeAttr("disabled");
		  $(`textarea[name="${key_array[i]}1_content"]`).removeAttr("disabled");
		});		
	}
	for (let j = 1; j < 9; j++) {
		$(`textarea[name="${key_array[i]}${j}_content"]`).change(function(){
		  $(`textarea[name="${key_array[i]}${j + 1}_content"]`).removeAttr("disabled");
		});
	}
}