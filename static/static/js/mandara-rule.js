let field_stop = '';
$('.input-table').attr('disabled', true);
$('.input-value-tab').attr('disabled', true);

function check() {

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
}
check()
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
	$('#id_field_stop').val('start_YYYYMM');
	if ($(this).val()) {
		$('#id_field_stop').val('A_keyword');
		$('input[name="A_keyword"]').removeAttr("disabled");
		$('input[name="A_keyword"]').focus();
	}
	findFieldStop();

});

var key_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
for (let i = 0; i < key_array.length; i++) {
	$(`textarea[name="${key_array[i]}_dueto"]`).change(function () {
		if (!$(this).val()) {
			$('#id_field_stop').val(`${key_array[i]}_dueto`);
			findFieldStop();
			return;
		}
		if (i < key_array.length - 1) {
			$(`input[name="${key_array[i + 1]}_keyword"]`).removeAttr("disabled");
			$('#id_field_stop').val(`${key_array[i + 1]}_keyword`);
		} else {
			$(`textarea[name="${key_array[0]}1_content"]`).removeAttr("disabled");
			$('#id_field_stop').val(`${key_array[0]}1_content`);
		}
		findFieldStop();
	});

	$(`input[name="${key_array[i]}_keyword"]`).change(function () {
		console.log($("#id_A_keyword").val());
		if ($("#id_A_keyword").val() && $("#id_B_keyword").val() && $("#id_C_keyword").val() && $("#id_D_keyword").val() && $("#id_E_keyword").val() && $("#id_F_keyword").val() && $("#id_G_keyword").val() && $("#id_H_keyword").val()) {

			$(".wrapper-top-block").css("display", "none")
			$(".title-main-score-top").css("display", "none")
		}
		if (!$(this).val()) {
			$('#id_field_stop').val(`${key_array[i]}_keyword`);
			findFieldStop();
			return;
		}
		if (i < key_array.length - 1) {
			$(`textarea[name="${key_array[i]}_dueto"]`).removeAttr("disabled");
			$('#id_field_stop').val(`${key_array[i]}_dueto`);
		} else {
			$(`textarea[name="${key_array[i]}_dueto"]`).removeAttr("disabled");
			$('#id_field_stop').val(`${key_array[i]}_dueto`);
		}
		findFieldStop();
	});
	for (let j = 1; j < 9; j++) {
		$(`textarea[name="${key_array[i]}${j}_content"]`).change(function () {
			if (!$(this).val()) {
				$('#id_field_stop').val(`${key_array[i]}${j}_content`);
				findFieldStop();
				return;
			}
			if (j < 8) {
				$(`textarea[name="${key_array[i]}${j + 1}_content"]`).removeAttr("disabled");
				$('#id_field_stop').val(`${key_array[i]}${j + 1}_content`);
			}
			if (j == 8 && i < key_array.length - 1) {
				$(`textarea[name="${key_array[i + 1]}1_content"]`).removeAttr("disabled");
				$('#id_field_stop').val(`${key_array[i + 1]}1_content`);
			}
			findFieldStop();
		});
	}

}

$(document).ready(function () {

	let flag = false;

	sort_fields.map(item => {
		if (!flag) {
			const valueTotal = $("#id_total_mission").val()
			if (valueTotal) {
				const valName = $(`[name="${item}"]`).val()

				if (!valName) {
					field_stop = item
					$(`#id_${item}`).focus().select();
					flag = true;
					check()
				}
			}

		}
	})

	$('#id_total_mission').on('keyup', function () {
		if ($("#id_total_mission").val()) {
			$('select[name="start_YYYYMM"]').attr("disabled", false);
			$('select[name="end_YYYYMM"]').attr("disabled", false);
		} else {
			$('select[name="start_YYYYMM"]').attr("disabled", true);
			$('select[name="end_YYYYMM"]').attr("disabled", true);
		}
	});

});

