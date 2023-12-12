var field_stop = $('#id_field_stop').val();
var sort_fields = ['total_mission', 'start_YYYYMM', 'end_YYYYMM', 'A_dueto', 'A_keyword', 'B_dueto', 'B_keyword', 'C_dueto', 'C_keyword',
	'D_dueto', 'D_keyword', 'E_dueto', 'E_keyword', 'F_dueto', 'F_keyword', 'G_dueto', 'G_keyword', 'H_dueto', 'H_keyword',
	'A1_content', 'A2_content', 'A3_content', 'A4_content', 'A5_content', 'A6_content', 'A7_content', 'A8_content',
	'B1_content', 'B2_content', 'B3_content', 'B4_content', 'B5_content', 'B6_content', 'B7_content', 'B8_content',
	'C1_content', 'C2_content', 'C3_content', 'C4_content', 'C5_content', 'C6_content', 'C7_content', 'C8_content',
	'D1_content', 'D2_content', 'D3_content', 'D4_content', 'D5_content', 'D6_content', 'D7_content', 'D8_content',
	'E1_content', 'E2_content', 'E3_content', 'E4_content', 'E5_content', 'E6_content', 'E7_content', 'E8_content',
	'F1_content', 'F2_content', 'F3_content', 'F4_content', 'F5_content', 'F6_content', 'F7_content', 'F8_content',
	'G1_content', 'G2_content', 'G3_content', 'G4_content', 'G5_content', 'G6_content', 'G7_content', 'G8_content',
	'H1_content', 'H2_content', 'H3_content', 'H4_content', 'H5_content', 'H6_content', 'H7_content', 'H8_content',
];

$('.input-table').attr('disabled', true);
$('.select').attr('disabled', true);
$('.input-value-tab').attr('disabled', true);

if (field_stop == 'total_mission') {
	$('textarea[name="total_mission"]').closest('.value-table-score').addClass('box-required');
} else {
	if (field_stop.includes('_content')) $(`textarea[name="${field_stop}"]`).closest('.value-table').addClass('box-required');
	if (field_stop.includes('_YYYYMM')) $(`select[name="${field_stop}"]`).addClass('box-required');
	if (field_stop.includes('_keyword')) $(`input[name="${field_stop}"]`).addClass('box-required');
	sort_fields.some(item => {
		$(`#id_${item}`).removeAttr("disabled");
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
	if (!$('select[name="start_YYYYMM"]').attr("disabled")) return;
	$('select[name="start_YYYYMM"]').addClass('box-required');
	$('#id_field_stop').val('start_YYYYMM');
	$('select[name="start_YYYYMM"]').removeAttr("disabled");
});

$('select[name="start_YYYYMM"]').change(function () {
	$('select[name="start_YYYYMM"]').removeClass('box-required');
	if (!$('select[name="end_YYYYMM"]').attr("disabled")) return;
	$('select[name="end_YYYYMM"]').removeAttr("disabled");
	$('select[name="end_YYYYMM"]').addClass('box-required');
	$('#id_field_stop').val('end_YYYYMM');

});

$('select[name="end_YYYYMM"]').change(function () {
	$('select[name="end_YYYYMM"]').removeClass('box-required');
	if (!$('input[name="A_keyword"]').attr("disabled")) return;
	$('input[name="A_keyword"]').removeAttr("disabled");
	$('input[name="A_keyword"]').addClass('box-required');
	$('#id_field_stop').val('A_keyword');
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
			$(`textarea[name="${key_array[0]}1_content"]`).closest('.value-table').addClass('box-required');
			$('#id_field_stop').val(`${key_array[0]}1_content`);
		}
	});

	$(`input[name="${key_array[i]}_keyword"]`).change(function () {
		$(`input[name="${key_array[i]}_keyword"]`).removeClass('box-required');
		console.log(i, key_array.length - 1);
		if (i < key_array.length - 1) {
			if (!$(`input[name="${key_array[i + 1]}_keyword"]`).attr("disabled")) return;
			$('#id_field_stop').val(`${key_array[i + 1]}_keyword`);
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
			$(`textarea[name="${key_array[i]}${j}_content"]`).closest('.value-table').removeClass("box-required");
			$('#id_field_stop').val('');
			if (j < 8) {
				if (!$(`textarea[name="${key_array[i]}${j + 1}_content"]`).attr("disabled")) return;
				$(`textarea[name="${key_array[i]}${j + 1}_content"]`).removeAttr("disabled");
				$(`textarea[name="${key_array[i]}${j + 1}_content"]`).closest('.value-table').addClass("box-required");
				$('#id_field_stop').val(`${key_array[i]}${j + 1}_content`);
			}
			if (j == 8 && i < key_array.length - 1) {
				if (!$(`textarea[name="${key_array[i + 1]}1_content"]`).attr("disabled")) return;
				$(`textarea[name="${key_array[i + 1]}1_content"]`).removeAttr("disabled");
				$(`textarea[name="${key_array[i + 1]}1_content"]`).closest('.value-table').addClass("box-required");
				$('#id_field_stop').val(`${key_array[i + 1]}1_content`);
			}
		});
	}
}
