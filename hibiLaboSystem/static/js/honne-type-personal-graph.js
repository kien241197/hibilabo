// 横軸のラベル
var xlabels           = ["A", "B", "C", "D", "E", "F", "G"];

// １つ目の系列の情報を設定
var series01name      = "データ１";                          // 系列１の名前
var series01data      = [ 10,  40,  10,  40,  10,  40,  10]; // 系列１データ
var series01bgcolor   = "rgba(255, 99, 132, 0.2)";           // 系列１の塗りつぶし色
var series01linecolor = "rgba(255, 99, 132, 1.0)";           // 系列１の線の色
// ２つ目の系列の情報を設定
var series02name      = "データ２";
var series02data      = [ 35,  15,  35,  15,  35,  15,  35];
var series02bgcolor   = "rgba(255, 200, 132, 0.2)";
var series02linecolor = "rgba(255, 200, 132, 1.0)";
// ３つ以上系列を描画する場合は上のセットを追加する

// グラフ縦軸の最大／最小／目盛りの間隔を設定
var ymax  = 100;  // グラフ縦軸の最大
var ymin  =  0;  // グラフ縦軸の最小
var ystep = 10;  // グラフ縦軸の目盛り線を引く間隔

var ctx = document.getElementById("str_canvas").getContext("2d");
var myChart1 = new Chart(ctx, {
  type: "bar",
  data: {
    labels: xlabels,
    datasets:[
      {
        label:           series01name,
        data:            series01data,
        backgroundColor: series01bgcolor,
        borderColor:     series01linecolor,
        borderWidth:     1,
      },
      {
        label:           series02name,
        data:            series02data,
        backgroundColor: series02bgcolor,
        borderColor:     series02linecolor,
        borderWidth:     1,
      }
      // ３つ以上系列を描画する場合は上のセットを追加する
    ]
  },
  options: {
    scales: {
      y: {
        display:      true,
        suggestedMax: ymax,
        suggestedMin: ymin,
        ticks: {
          stepSize: ystep,
        },
      }
    }
  }
});