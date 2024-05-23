let field_stop = '';

function check() {

		if (field_stop.includes('_content')) $(`textarea[name="${field_stop}"]`).addClass('box-required');
		if (field_stop.includes('_dueto')) $(`textarea[name="${field_stop}"]`).addClass('box-required');
		if (field_stop.includes('_YYYYMM')) $(`select[name="${field_stop}"]`).addClass('box-required');
		if (field_stop.includes('_keyword')) $(`input[name="${field_stop}"]`).addClass('box-required');
}

$('input[name="save"').click(function () {
	$('textarea[name="total_mission"]').attr('required', true);
	$('.input-table').attr('required', true);
	$('.select').attr('required', true);
	$('.input-value-tab').attr('required', true);
});
$('input[name="save_tmp"').click(function () {
	$('textarea[name="total_mission"]').removeAttr('required');
	$('.input-table').removeAttr('required');
	$('.select').removeAttr('required');
	$('.input-value-tab').removeAttr('required');
});


$('select[name="start_YYYYMM"]').change(function () {
	$('#id_field_stop').val('start_YYYYMM');
	$(`#id_start_YYYYMM`).focus().select();
	findFieldStop();

});

var key_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
for (let i = 0; i < key_array.length; i++) {

	$(`input[name="${key_array[i]}_keyword"]`).change(function () {
		if ($("#id_A_keyword").val() && $("#id_B_keyword").val() && $("#id_C_keyword").val() && $("#id_D_keyword").val() && $("#id_E_keyword").val() && $("#id_F_keyword").val() && $("#id_G_keyword").val() && $("#id_H_keyword").val()) {

			$(".wrapper-top-block").css("display", "none")
			$(".title-main-score-top").css("display", "none")
		}
	});

}

$(document).ready(function () {

	let flag = false;

	$(`#id_total_mission`).focus().select();
	sort_fields.map(item => {
		if (!flag) {
			const valueTotal = $("#id_total_mission").val()
			if (valueTotal) {
				const valName = $(`#id_${item}`).val()
				if (!valName) {

					field_stop = item

					$(`#id_${item}`).focus().select();
					flag = true;
					check()
				}
			}

		}
	})

});

