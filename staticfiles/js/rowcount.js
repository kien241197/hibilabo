		function func_count(){
			var mytable = document.getElementById("td1");
			var resulttable = document.getElementById("calc_resul");
			var int_counter = 0;
			var array_group = new Array(7);
			for ( var i=0; i <= 7; i++){
				array_group[i]=0;
			}

			//合計行の数字を書き換え
			mytable.rows[51].cells[2].innerHTML = int_counter;