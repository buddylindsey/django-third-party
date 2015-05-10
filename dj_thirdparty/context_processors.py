import re

from dj_thirdparty.models import CustomContent


__all__ = ['custom_content']


def set_header_footer_content(collection, js):
    if js.header:
        collection['header'].append(js)
    else:
        collection['footer'].append(js)


def fetch_objects():
    all_objects = CustomContent.objects.filter(active=True)
    url_shortcuts = ['all']
    all_urls = {'header': [], 'footer': []}
    exact_urls = {'header': [], 'footer': []}
    partial_urls = {'header': [], 'footer': []}

    for obj in all_objects.iterator():
        in_shortcut = obj.path in url_shortcuts

        if obj.path == 'all':
            set_header_footer_content(all_urls, obj)
        elif obj.exact_match and (not in_shortcut) and not obj.partial_match:
            set_header_footer_content(exact_urls, obj)
        elif obj.partial_match and (not in_shortcut) and not obj.exact_match:
            set_header_footer_content(partial_urls, obj)

    return {
        'all_urls': all_urls,'exact_urls': exact_urls,
        'partial_urls': partial_urls}


def final_content(location, request, custom_js):
    final_javascript = ""
    final_javascript += "".join(
        [js.javascript for js in custom_js['all_urls'][location]])
    final_javascript += "".join(
        [js.javascript for js in custom_js['exact_urls'][location]
            if js.path == request.path])
    final_javascript += "".join(
        [js.javascript for js in custom_js['partial_urls'][location]
            if re.compile(js.path).search(request.path)])
    return final_javascript


def custom_content(request):
    if not request:
        return {}
    custom = fetch_objects()

    return {'custom_javascript_footer': final_content('footer',
                                                      request, custom),
            'custom_javascript_header': final_content('header',
                                                      request, custom)}
