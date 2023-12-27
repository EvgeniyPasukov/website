const setLabel = (lbl, val) => {
  const label = $(`#slider-${lbl}-label`);
  label.text(val);
  const slider = $(`#slider-div .${lbl}-slider-handle`);
  const rect = slider[0].getBoundingClientRect();
  label.offset({

  });
}

const setLabels = (values) => {
  setLabel("min", values[1]);
  setLabel("max", values[0]);
}


$('#ex2').slider().on('slide', function(ev) {
  setLabels(ev.value);
});
setLabels($('#ex2').attr("data-value").split(","));