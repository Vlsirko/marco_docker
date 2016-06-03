angular.module('services', ['ngResource'])
    .factory('Category', function ($resource) {
        return $resource('/api/category/:slug/', {slug: '@slug'});
    })
    .factory('Slider', function ($resource) {
        return $resource('/api/slider/:id/', {id: '@id'});
    })

    .factory('User', function ($resource) {
        return $resource('/api/user/:id/', {id: '@id'});
    })

    .factory('Order', function ($resource) {
        return $resource('/api/order/:id/', {id: '@id'});
    })

    .factory('Page', function ($resource) {
        return $resource('/api/page/:id/', {id: '@id'});
    })

    .factory('Email', function ($resource) {
        return $resource('/api/email/', {}, {
            'send': {
                method: 'POST'
            }
        });
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
                    category__id: '@category_id'
                }
            },

            'search': {
                method: 'GET',
                params: {
                    search: '@search'
                }
            }
        });
    })
    .config(function ($resourceProvider) {
        $resourceProvider.defaults.stripTrailingSlashes = false;
    });