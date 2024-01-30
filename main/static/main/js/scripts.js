function ajaxSend(url, params) {
    // Отправляем запрос
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
}

 Filter catalog
 const forms = document.querySelector('form[name=filter]');

 forms.addEventListener('submit', function (e) {
     // Получаем данные из формы
     e.preventDefault();
     let url = this.action;
     let params = new URLSearchParams(new FormData(this)).toString();
     ajaxSend(url, params);
 });

function render(data) {
    // Рендер шаблона
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('.left-ads-display>.row');
    div.innerHTML = output;
}

let html = '\
{{#catalog}}\
    <div class="product-card">
                    <div class="product-thumb">
                        <a href="/{{ url }}"><img src="media/{{ image }}" alt=""></a>
                    </div>
                    <div class="product-details">
                        <div class="product-bottom-details d-flex justify-content-center">
                            <h4><a href="/{{ url }}">/{{ name }}</a></h4>
                        </div>
                    </div>
                </div>
{{/catalog}}'
