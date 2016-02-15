/**
 * Created by woongkaa on 2016. 2. 15..
 */
window.onload = function onLoad(){
    var startColor = '#FC5B3F';
    var endColor = '#337AB7';

    var element = document.getElementById('ps-percent-container');
    var circle = new ProgressBar.Circle(element, {
        color: startColor,
        trailColor: '#eee',
        trailWidth: 1,
        duration: 1500,
        easing: 'bounce',
        strokeWidth: 3,
        text: {
            value: '0'
        },

        // Set default step function for all animate calls
        step: function(state, bar) {
            bar.setText((bar.value() * 100).toFixed(2) + '%');
            bar.path.setAttribute('stroke', state.color);
        }
    });

    circle.animate(window.percentage, {
        from: {color: startColor},
        to: {color: endColor}
    });
}