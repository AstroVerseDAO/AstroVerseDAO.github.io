/* ============================================================
   星宙 · 观星书院 —— 交互层
   1. Canvas 星野：视差 + 闪烁 + 偶发流星
   2. 滚动揭示（IntersectionObserver）
   3. 顶栏滚动态
   4. 机制轨道描线（随滚动生长）
   5. 首页星座图：悬停点亮相邻星轨
   ============================================================ */

(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- 1. 星野 ---------- */
  var canvas = document.getElementById('sky');
  if (canvas) {
    var ctx = canvas.getContext('2d');
    var stars = [];
    var meteors = [];
    var W = 0, H = 0, DPR = Math.min(window.devicePixelRatio || 1, 2);
    var mouseX = 0.5, mouseY = 0.5;

    function resize() {
      W = window.innerWidth; H = window.innerHeight;
      canvas.width = W * DPR; canvas.height = H * DPR;
      canvas.style.width = W + 'px'; canvas.style.height = H + 'px';
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
      seed();
    }

    function seed() {
      stars = [];
      var count = Math.floor((W * H) / 9000);
      for (var i = 0; i < count; i++) {
        stars.push({
          x: Math.random() * W,
          y: Math.random() * H,
          r: Math.random() * 1.1 + 0.2,
          depth: Math.random() * 0.8 + 0.2,
          phase: Math.random() * Math.PI * 2,
          speed: Math.random() * 0.6 + 0.2,
          warm: Math.random() < 0.18
        });
      }
    }

    function spawnMeteor() {
      var fromLeft = Math.random() < 0.5;
      meteors.push({
        x: fromLeft ? -60 : W * (0.4 + Math.random() * 0.6),
        y: Math.random() * H * 0.35,
        vx: (fromLeft ? 1 : -1) * (3.2 + Math.random() * 2.2),
        vy: 1.6 + Math.random() * 1.2,
        life: 1
      });
    }

    var t = 0, frame = 0;

    function draw() {
      ctx.clearRect(0, 0, W, H);
      t += 0.016; frame++;

      var px = (mouseX - 0.5), py = (mouseY - 0.5);

      for (var i = 0; i < stars.length; i++) {
        var s = stars[i];
        var tw = 0.45 + 0.55 * Math.abs(Math.sin(s.phase + t * s.speed));
        var x = s.x - px * 26 * s.depth;
        var y = s.y - py * 26 * s.depth;
        ctx.beginPath();
        ctx.arc(x, y, s.r, 0, Math.PI * 2);
        ctx.fillStyle = s.warm
          ? 'rgba(196, 224, 160,' + (tw * 0.85).toFixed(3) + ')'
          : 'rgba(214, 230, 205,' + (tw * 0.7).toFixed(3) + ')';
        ctx.fill();
      }

      if (!reduced && frame % 60 === 0 && Math.random() < 0.12 && meteors.length < 2) {
        spawnMeteor();
      }
      for (var j = meteors.length - 1; j >= 0; j--) {
        var m = meteors[j];
        m.x += m.vx; m.y += m.vy; m.life -= 0.012;
        if (m.life <= 0 || m.x < -120 || m.x > W + 120 || m.y > H + 60) {
          meteors.splice(j, 1); continue;
        }
        var grad = ctx.createLinearGradient(m.x, m.y, m.x - m.vx * 14, m.y - m.vy * 14);
        grad.addColorStop(0, 'rgba(196, 224, 160,' + (m.life * 0.9).toFixed(3) + ')');
        grad.addColorStop(1, 'rgba(196, 224, 160, 0)');
        ctx.strokeStyle = grad;
        ctx.lineWidth = 1.2;
        ctx.beginPath();
        ctx.moveTo(m.x, m.y);
        ctx.lineTo(m.x - m.vx * 14, m.y - m.vy * 14);
        ctx.stroke();
      }

      requestAnimationFrame(draw);
    }

    function drawStatic() {
      ctx.clearRect(0, 0, W, H);
      for (var i = 0; i < stars.length; i++) {
        var s = stars[i];
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(214, 230, 205, 0.55)';
        ctx.fill();
      }
    }

    window.addEventListener('resize', resize);
    window.addEventListener('mousemove', function (e) {
      mouseX = e.clientX / W; mouseY = e.clientY / H;
    }, { passive: true });

    resize();
    if (reduced) { drawStatic(); } else { draw(); }
  }

  /* ---------- 2. 滚动揭示 ---------- */
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) {
        en.target.classList.add('in');
        io.unobserve(en.target);
      }
    });
  }, { threshold: 0.15 });
  document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });

  /* ---------- 3 & 4. 顶栏 + 轨道描线 ---------- */
  var topbar = document.querySelector('.topbar');
  var orbitTrack = document.querySelector('.orbit-track');
  var orbitFill = document.getElementById('orbit-fill');

  function onScroll() {
    if (topbar) topbar.classList.toggle('scrolled', window.scrollY > 40);

    if (orbitTrack && orbitFill) {
      var rect = orbitTrack.getBoundingClientRect();
      var vh = window.innerHeight;
      var progress = (vh * 0.8 - rect.top) / (rect.height + vh * 0.35);
      progress = Math.max(0, Math.min(1, progress));
      orbitFill.style.height = (progress * 100) + '%';
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- 5. 星座图悬停联动 ---------- */
  var constellation = document.querySelector('.constellation');
  if (constellation) {
    constellation.querySelectorAll('a[data-d]').forEach(function (node) {
      node.addEventListener('mouseenter', function () {
        constellation.setAttribute('data-hover', node.getAttribute('data-d'));
      });
      node.addEventListener('mouseleave', function () {
        constellation.removeAttribute('data-hover');
      });
      node.addEventListener('focus', function () {
        constellation.setAttribute('data-hover', node.getAttribute('data-d'));
      });
      node.addEventListener('blur', function () {
        constellation.removeAttribute('data-hover');
      });
    });
  }
})();
