layui.use(['layer', 'carousel'], function () {
    var layer = layui.layer;
    var carousel = layui.carousel;
    layer.msg('试试');

    carousel.render({
        elem: '#carousel'
        , width: '1060px'
        , arrow: 'hover'
        , height: '600px'
        , interval: 5000
    });

});

const NumPerYearData = [
    {year: '1991', value: 3},
    {year: '1992', value: 4},
    {year: '1993', value: 3.5},
    {year: '1994', value: 5},
    {year: '1995', value: 4.9},
    {year: '1996', value: 6},
    {year: '1997', value: 7},
    {year: '1998', value: 9},
    {year: '1999', value: 13}
];

const NumPerYear = new G2.Chart({
    container: 'num-per-year',
    width: 1000,
    height: 500
});

NumPerYear.source(NumPerYearData);
NumPerYear.scale('value', {
    min: 0
});
NumPerYear.scale('year', {
    range: [0, 1]
});
NumPerYear.tooltip({
    crosshairs: {
        type: 'line'
    }
});
NumPerYear.line().position('year*value');
NumPerYear.point().position('year*value').size(4).shape('circle').style({
    stroke: '#fff',
    lineWidth: 1
});
NumPerYear.render();

const ProtocolData = [
    {year: '2001', population: 41.8},
    {year: '2002', population: 38},
    {year: '2003', population: 33.7},
    {year: '2004', population: 30.7},
    {year: '2005', population: 25.8},
    {year: '2006', population: 31.7},
    {year: '2007', population: 33},
    {year: '2008', population: 46},
    {year: '2009', population: 38.3},
    {year: '2010', population: 28},
    {year: '2011', population: 42.5},
    {year: '2012', population: 30.3}
];

const Protocol = new G2.Chart({
    container: 'protocol',
    width: 1000,
    height: 500
});
Protocol.source(data);
Protocol.coord('polar', {
    innerRadius: 0.2
});
Protocol.legend({
    position: 'right',
    offsetY: -40,
    offsetX: -200
});
Protocol.axis(false);
Protocol.interval().position('license*num')
    .color('license', G2.Global.colors_pie_16)
    .style({
        lineWidth: 1,
        stroke: '#fff'
    });
Protocol.render();

