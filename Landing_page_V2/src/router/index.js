import { createRouter, createWebHistory } from 'vue-router';

const routes = [
	{
		path: '/',
		name: 'Accueil',
		component: () => import('../views/Home.vue'),
	},
	{
		path: '/fonctionnalites',
		name: 'Fonctionnalités',
		component: () => import('../views/Features.vue'),
	},
	{
		path: '/demo',
		name: 'Démo',
		component: () => import('../views/Demo.vue'),
	},
	{
		path: '/a-propos',
		name: 'A propos',
		component: () => import('../views/About.vue'),
	},
  {
		path: '/profil',
		name: 'Profil',
		component: () => import('../views/Profil.vue'),
	},
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;
