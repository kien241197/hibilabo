let field_stop = $('#id_field_stop').val();
$('.input-table').attr('disabled', true);
$('.input-value-tab').attr('disabled', true);

if (field_stop == 'total_mission') {
	$('textarea[name="total_mission"]').closest('.value-table-score').addClass('box-required');
} else {
	if (field_stop.includes('_content')) $(`textarea[name="${field_stop}"]`).addClass('box-required');
	if (field_stop.includes('_dueto')) $(`textarea[name="${field_stop}"]`).addClass('box-required');
	if (field_stop.includes('_YYYYMM')) $(`select[name="${field_stop}"]`).addClass('box-required');
	if (field_stop.includes('_keyword')) $(`input[name="${field_stop}"]`).addClass('box-required');

	sort_fields.map(item => {
		$(`#id_${item}`).attr("disabled", false);
		if (item == field_stop) return true;
	})
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
$('textarea[name="total_mission"]').change(function () {
	$('textarea[name="total_mission"]').closest('.value-table-score').removeClass('box-required');
	$('select[name="start_YYYYMM"]').addClass('box-required');
});


$('select[name="start_YYYYMM"]').change(function () {
	$('select[name="start_YYYYMM"]').removeClass('box-required');
	$('input[name="A_keyword"]').removeAttr("disabled");
	$('input[name="A_keyword"]').addClass('box-required');
	$('input[name="A_keyword"]').focus();
	// $('#id_field_stop').val('A_keyword');

});

var key_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
for (let i = 0; i < key_array.length; i++) {
	$(`textarea[name="${key_array[i]}_dueto"]`).change(function () {

		$(`textarea[name="${key_array[i]}_dueto"]`).removeClass('box-required');
		if (i < key_array.length - 1) {
			if (!$(`input[name="${key_array[i + 1]}_keyword"]`).attr("disabled")) return;
			$(`input[name="${key_array[i + 1]}_keyword"]`).addClass('box-required');
			$(`input[name="${key_array[i + 1]}_keyword"]`).removeAttr("disabled");
		} else {
			if (!$(`textarea[name="${key_array[0]}1_content"]`).attr("disabled")) return;
			$(`textarea[name="${key_array[0]}1_content"]`).removeAttr("disabled");
			$(`textarea[name="${key_array[0]}1_content"]`).addClass('box-required');
			// $('#id_field_stop').val(`${key_array[0]}1_content`);
		}
	});

	$(`input[name="${key_array[i]}_keyword"]`).change(function () {
		$(`input[name="${key_array[i]}_keyword"]`).removeClass('box-required');
		console.log(i, key_array.length - 1);
		console.log($("#id_A_keyword").val());
		if ($("#id_A_keyword").val() && $("#id_B_keyword").val() && $("#id_C_keyword").val() && $("#id_D_keyword").val() && $("#id_E_keyword").val() && $("#id_F_keyword").val() && $("#id_G_keyword").val() && $("#id_H_keyword").val()) {

			$(".wrapper-top-block").css("display", "none")
		}
		if (i < key_array.length - 1) {
			if (!$(`input[name="${key_array[i + 1]}_keyword"]`).attr("disabled")) return;
			// $('#id_field_stop').val(`${key_array[i + 1]}_keyword`);
			if (!$(`textarea[name="${key_array[i]}_dueto"]`).attr("disabled")) return;
			$(`textarea[name="${key_array[i]}_dueto"]`).addClass("box-required");
			$(`textarea[name="${key_array[i]}_dueto"]`).removeAttr("disabled");
		} else {
			if (!$(`textarea[name="${key_array[i]}_dueto"]`).attr("disabled")) return;
			$(`textarea[name="${key_array[i]}_dueto"]`).addClass("box-required");
			$(`textarea[name="${key_array[i]}_dueto"]`).removeAttr("disabled");
		}
	});
	for (let j = 1; j < 9; j++) {
		$(`textarea[name="${key_array[i]}${j}_content"]`).change(function () {
			$(`textarea[name="${key_array[i]}${j}_content"]`).removeClass("box-required");
			// $('#id_field_stop').val('');
			if (j < 8) {
				if (!$(`textarea[name="${key_array[i]}${j + 1}_content"]`).attr("disabled")) return;
				$(`textarea[name="${key_array[i]}${j + 1}_content"]`).removeAttr("disabled");
				$(`textarea[name="${key_array[i]}${j + 1}_content"]`).addClass("box-required");
				// $('#id_field_stop').val(`${key_array[i]}${j + 1}_content`);
			}
			if (j == 8 && i < key_array.length - 1) {
				if (!$(`textarea[name="${key_array[i + 1]}1_content"]`).attr("disabled")) return;
				$(`textarea[name="${key_array[i + 1]}1_content"]`).removeAttr("disabled");
				$(`textarea[name="${key_array[i + 1]}1_content"]`).addClass("box-required");
				// $('#id_field_stop').val(`${key_array[i + 1]}1_content`);
			}
		});
	}

}

$(document).ready(function () {

	// let flag = false;

	// sort_fields.map(item => {
	// 	if (!flag) {
	// 		const valName = $(`[name="${item}"]`).val()

	// 		if (!valName) {
	// 			console.log("Vào đây", item)
	// 			field_stop = $('#id_field_stop').val(item)
				
	// 			flag = true;
	// 		}
	// 	}
	// })

	$('#id_total_mission').on('keyup', function () {
		if ($("#id_total_mission").val()) {
			$('select[name="start_YYYYMM"]').attr("disabled", false);
			$('select[name="end_YYYYMM"]').attr("disabled", false);
		} else {
			$('select[name="start_YYYYMM"]').attr("disabled", true);
			$('select[name="end_YYYYMM"]').attr("disabled", true);
		}
	});

	$('textarea').change(function () {
		const textareaName = $(this).attr('name');

		if (!$(this).val()) {
			$('#id_field_stop').val(textareaName);
		}
	});

	$('input').change(function () {
		const inputName = $(this).attr('name');

		if (!$(this).val()) {
			$('#id_field_stop').val(inputName);
		}
	});

	$('select').c(function () {
		const inputName = $(this).attr('name');
		if (!$(this).val()) {
			console.log("inputName", $(this).val());
			$('#id_field_stop').val(inputName);
		}
	});
});

