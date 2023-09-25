<div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="">
<div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class=""><main id="js-repo-pjax-container"><turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
<div id="repo-content-pjax-container" class="repository-content ">
<div class="clearfix container-xl px-md-4 px-lg-5 px-3 mt-4">
<div data-view-component="true" class="Layout Layout--flowRow-until-md Layout--sidebarPosition-end Layout--sidebarPosition-flowRow-end">
<div data-view-component="true" class="Layout-main"><readme-toc data-catalyst="">
<div id="readme" class="Box md js-code-block-container js-code-nav-container js-tagsearch-file Box--responsive" data-tagsearch-path="README.md" data-tagsearch-lang="Markdown">
<div data-target="readme-toc.content" class="Box-body px-5 pb-5">
<article class="markdown-body entry-content container-lg" itemprop="text">
<h1 align="center" id="user-content-итоговый-проект-по-разделу-автоматизация-тестирования-" dir="auto" tabindex="-1">Итоговый проект по автоматизации тестирования</h1>
<ul dir="auto">
<li>Объект тестирования:<span>&nbsp;</span><a href="https://b2c.passport.rt.ru/" rel="nofollow">https://b2c.passport.rt.ru/</a></li>
<li>Требования к проекту:<span>&nbsp;</span><a href="https://lms.skillfactory.ru/assets/courseware/v1/f78e146f0eb3ace247a28b07e66467de/asset-v1:SkillFactory+INTQAP+2022+type@asset+block/%D0%A2%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_SSO_%D0%B4%D0%BB%D1%8F_%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_last.doc" rel="nofollow">Требования</a></li>
</ul>
<p dir="auto"><strong>Техническое задание Заказчика:</strong></p>
<ol dir="auto">
<li>
<p dir="auto">&nbsp;Протестировать требования.</p>
</li>
<li>
<p dir="auto">Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.</p>
</li>
<li>
<p dir="auto">Провести автоматизированное тестирование продукта (не менее 15 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.</p>
</li>
<li>
<p dir="auto">Оформить описание обнаруженных дефектов. Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов. Если дефекты не обнаружены, то подумайте и опишите 3 потенциально возможных дефекта на данном ресурсе.</p>
</li>
</ol>
<p dir="auto"><strong>Примененые методы при разработке проекта:</strong></p>
<p dir="auto">Для разработки тест-кейсов использованы методы "черного ящика", функционального тестирование, UX тестирование. Так же использованы техники тест дизайна : диаграмма состояний и переходов, классы эквивалентности, граничные значения и попарное тестирование.</p>
<p dir="auto">Разработка проекта автотестирования выполнена по паттерну PageObject. Для разработки автотестов применялись библиотеки pytest, pytest-selenium. Использовались фикстуры, фикстуры параметризации, явные и неявные ожидания драйвером, различные способы описания локаторов (СSS_SELECTOR, XPATH, ID, CLASS_NAME, NAME). Проект разработан для операционной системы macOS и ей подобных.</p>
<h2 id="user-content-структура-проекта" dir="auto" tabindex="-1">Структура проекта:</h2>
<h3 id="user-content-директория-page-содержит" dir="auto" tabindex="-1">Директория page содержит:</h3>
<p dir="auto">base_page.py - описание атрибутов и методов работы с базовой страницей.<br />auth_page.py - описание атрибутов и методов работы со страницей авторизации проекта.<br />reg_page.py - описание атрибутов и методов работы со страницей регистрации проекта.<br />reset_page.py - описание атрибутов и методов работы со страницей восстановления пароля проекта.<br />locators.py - описание локаторов проекта.</p>
<h3 id="user-content-директория-tests-содержит" dir="auto" tabindex="-1"><turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class=""><readme-toc data-catalyst="">
<h3 id="user-content-директория-page-содержит" dir="auto" tabindex="-1">Директория tests содержит:</h3>
</readme-toc></turbo-frame></h3>
<p dir="auto">test_auth_page.py - тесты страницы авторизации проекта.<br />test_reg_page.py - тесты страницы регистрации проекта.<br />test_reset_page.py - тесты страницы восстановления пароля проекта.<br />config.py - описание значений элементов страниц и переменных.<br />conftest.py - описание фикстур для проекта.<br />pytest.ini - файл конфигурации Pytest.</p>
<h2 id="user-content-запуск-тестов-производится-из-терминала-следующими-командами" dir="auto" tabindex="-1"><turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class=""><readme-toc data-catalyst="">
<h2 id="user-content-запуск-тестов-производится-из-терминала-следующими-командами" dir="auto" tabindex="-1"><strong>Запуск тестов производится из терминала следующими командами:</strong></h2>
</readme-toc></turbo-frame></h2>
<ol dir="auto">
<li>
<p dir="auto">Для тестов страницы авторизации: python3 -m pytest -v --driver Chrome --driver-path /driver/chromedriver tests/test_auth_page.py</p>
</li>
<li>
<p dir="auto">Для тестов страницы регистрации: python3 -m pytest -v --driver Chrome --driver-path /driver/chromedriver tests/test_reg_page.py</p>
</li>
<li>
<p dir="auto">Для тестов страницы восстановления пароля: python3 -m pytest -v --driver Chrome --driver-path /driver/chromedriver tests/test_reset_page.py</p>
</li>
</ol>
</article>
</div>
</div>
</readme-toc></div>
<div data-view-component="true" class="Layout-sidebar">
<div class="BorderGrid BorderGrid--spacious" data-pjax="">
<div class="BorderGrid-row hide-sm hide-md">
<div class="BorderGrid-cell"></div>
</div>
</div>
</div>
</div>
</div>
</div>
</turbo-frame></main></div>
</div>
<footer class="footer width-full container-xl p-responsive" role="contentinfo">
<div class="position-relative d-flex flex-items-center pb-2 f6 color-fg-muted border-top color-border-muted flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap mt-6 pt-6"><nav aria-label="Footer" class="col-12 col-lg-8"></nav></div>
</footer>
