angular.module('services', ['ngResource'])
    .factory('Category', function ($resource) {
        return $resource('/api/category/:slug/', {slug: '@slug'});
    })
    .factory('Slider', function ($resource) {
        return $resource('/api/slider/:id/', {id: '@id'});
    })
    .factory('Product', function ($resource) {
        return $resource('/api/products/:slug/', {slug: '@slug'}, {

            'getNew': {
                method: 'GET',
                params: {
                    page_size: 9,
                    is_new: 'True',
                    ordering: '-time_add'
                }
            },

            'getSale': {
                method: 'GET',
                params: {
                    page_size: 9,
                    is_sale: 'True',
                    ordering: '-time_add'
                }
            },

            'getByCategorySlug': {
                method: 'GET',
                params: {
                    category__url: '@category_url'
                }
            }
        });
    })
    .config(function ($resourceProvider) {
        $resourceProvider.defaults.stripTrailingSlashes = false;
    });