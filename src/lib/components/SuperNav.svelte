<script lang="ts">
    import Topnav from "./Topnav.svelte";
    import BottomNav from "./BottomNav.svelte";
    import Navbar from "./Navbar.svelte";
    
    let { navItems, logo } = $props();

    let lastScrollY = $state(0);
    let topVisible = $state(true);
    let bottomHidden = $state(false);

    function handleScroll() {
        const currentScrollY = window.scrollY;
        topVisible = currentScrollY < lastScrollY || currentScrollY < 10;
        bottomHidden = currentScrollY > lastScrollY && currentScrollY > 100;
        lastScrollY = currentScrollY;
    }
</script>

<svelte:window onscroll={handleScroll} />

<div class="lg:hidden h-30"></div>
<Navbar {navItems} {logo} />
<Topnav {navItems} {logo} {topVisible} />
<BottomNav {navItems} {bottomHidden} />