angular.module('MirrorStore.page', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/contacts', {
            templateUrl: 'page/contacts.html',
            controller: 'contactsCtrl'
        }).when('/delivery', {
            templateUrl: 'page/delivery.html',
            controller: 'deliveryCtrl'
        }).when('/payments', {
            templateUrl: 'page/payments.html',
            controller: 'paymentsCtrl'
        });
    }])

    .controller('contactsCtrl', function ($rootScope) {
        $rootScope.title = 'MirrorStore: Контакты';

    }).controller('deliveryCtrl', function ($rootScope) {
        $rootScope.title = 'MirrorStore: Доставка';

    }).controller('paymentsCtrl', function ($rootScope) {
        $rootScope.title = 'MirrorStore: Оплата';
    });