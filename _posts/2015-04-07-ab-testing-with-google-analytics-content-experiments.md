---
layout: post
title: "A/B Testing with Google Analytics Content Experiments"
date: 2015-04-07
---
If you’re anything like me, you’ve wanted to play around with A/B testing for
years but never gotten around to it. I finally decided to do some experiments
with my Wealthfront affiliate site at
[http://wealthfrontinvite.com](http://wealthfrontinvite.com/). It’s the
simplest landing page you can imagine – users just need to click a button.
There are no fields to fill out or email addresses to enter.

In college I studied Information Systems, and there is a very active alumni
email list that I still participate in. I wrote up the following email:

> I built an affiliate site for Wealthfront, an investment service. The
> affiliate site works fairly well as-is, but I would like to do some A/B
> testing to optimize it (I’ve never done A/B testing and I would like to
> learn).
>
> I purchased 4 different domains.
>
>   * http://wealthfrontinvite.com
>   * http://wealthfrontreferral.com
>   * http://wealthfrontcouponcode.com
>   * http://wealthfrontpromocode.com
>

>
> My question is how I should approach A/B testing. I want to test both which
> domain is the most effective, and then different screen layouts/text/colors.
> Since the website is so simple this doesn’t need to be a heavyweight
> solution. It’s essentially just A/B testing a landing page.
>
> I’ve done some searching and found a few tools that will do this, but wanted
> to get the list’s insight and experience as to what you’ve done, how you
> would approach this, and what has been most effective.

The responses covered the more popular tools such as
[Unbounce](http://unbounce.com/), [Optimizely](https://www.optimizely.com/),
and [Visual Website Optimizer](https://vwo.com/). However, those tools are all
fairly expensive when you’ve only got one landing page and there isn’t any
real money coming in from it.

[Michael Eads](https://www.linkedin.com/profile/view?id=38237847) replied with
the winning answer:

> Great idea Derek… wealthfront rocks!
>
> For this project I would go with ga’s built in “Content Experiments” feature
> (formerly Google Website Optimizer). It’s a free testing platform integrated
> directly into Google Analytics. VWO or Optimizely might be a little easier
> but since you obviously are technically savvy, Google’s built in feature
> could be a good way to go since you want to be using ga anyway (and not
> really any more difficult).
>
> Or you could just set up a standard “Goal” so you are tracking conversion
> for each of your four sites and use each site as a different test. A little
> more a hack imo but would give you an idea of if one is working better than
> the other, assuming the visitors to each of the sites are coming via the
> same channel.
>
> Some tests to try:
>  – Main headline.. could try a more benefit-focus as the headline, instead
> of “GET YOUR WEALTHFRONT INVITE HERE” you could try something like, “The no-
> lose way to increase the assets managed for free” That one isn’t necessarily
> any good but focusing more on the benefit might be something to try.
>  – The button’s CTA. I was a little unsure what the green download looking
> button was. You might try something like “get my invite now” to make or
> somehow make it more obvious that is where you want visitors to click
> (button color is also fun to try)
>  – The background image (I like the one you have but you might try one with
> a pretty face or two)
>
> How are you driving traffic? seo?
>  Depending on what people are searching for you might get a lift by matching
> the copy to what the person was originally searching for. E.g. if someone
> was searching for “Wealthfront Coupon Code” then you could use the headline
> “Get your wealthfront coupon here” to make it more congruent with where they
> came from.
>
> Cheers
>  Mike
>
> ps a good website to nerd out on this stuff is ConversionXL

Michael’s input was spot on. Google Analytics Content Experiments were the
right way to go for me because I wanted something free yet powerful, and I was
willing to design the pages myself.

I implemented one of Mike’s suggestions before even starting the experiment.
The conversion button I was using was awful. It blended in with the background
and was actually an old “download” button I hadn’t bothered to change. Some
searching led me to a great free [Call-to-Action Button
Generator](http://buttonoptimizer.com/) which I used to generate a bright
green button.

Step 1 was to set up Google Analytics. I already had it running on
[http://wealthfrontinvite.com](http://wealthfrontinvite.com/) but didn’t on
the other three domains. They had previously just redirected to the same files
on the server. For this experiment I had to point them to different folders
and copy the site into them. The repointing was actually a difficult thing to
do with my hosting provider, HostMonster. I won’t go into the details, but
there’s an easy and quick way that is supposed to work but that no longer
works since they launched their redesigned site, which is so hideously ugly
I’m tempted to change hosting providers just because it hurts my eyes now. I
had to unassign and reassign each of the three domains to my account.

There are lots of tutorials on setting up Google Analytics and it’s very
intuitive (just paste some JavaScript into your page), so I won’t go into that
here.

> <script>// <![CDATA[
>
> (function(i,s,o,g,r,a,m){i[‘GoogleAnalyticsObject’]=r;i[r]=i[r]||function(){
>  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new
> Date();a=s.createElement(o),
>
> m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
>  })(window,document,’script’,’//www.google-
> analytics.com/analytics.js’,’ga’);
>
> ga(‘create’, ‘YOURCODEHERE’, ‘auto’);
>  ga(‘send’, ‘pageview’);
>  // ]]></script>

Step 2 was to create a Goal in Google Analytics which would allow me to track
success at the thing I was trying to accomplish. I wanted people to click on a
button, which I thought should be simple to set as a goal. It wasn’t as
intuitive as I hoped.

The first problem to overcome was to figure out how to track a button click. I
thought this would happen automatically when I set up Google Analytics, but it
didn’t. After some [DuckDuckGo-ing](https://duckduckgo.com/) (if you’re still
using Google, you should switch) I came across the free [Google Analytics
Configuration Tool](http://gaconfig.com/) made by [Raven Internet Marketing
Tools](http://raventools.com/). This showed me how to set up the button click
as an Event, then tell Google Analytics how to look out for that Event.

Once the event was in the system, creating a goal was easy. Goal = event
happening.

![Screen Shot 2015-04-02 at 10.59.06
PM](https://i0.wp.com/www.derekchristensen.com/wp-
content/uploads/2015/04/Screen-
Shot-2015-04-02-at-10.59.06-PM-1024x481.png?resize=940%2C442)

Step 3 was to build out different variations of the page. I got some some
awesome background images from [Unsplash](https://unsplash.com/), the BEST
stock photography site on the web. I copied the index.html page as well as
style.css, and then created 5 variations with different backgrounds and/or
different color buttons. It’s best to only change one variable at a time so
you can accurately attribute the performance difference to something specific,
but I did change two variables in some of these experiments. Not best
practice.

You can see all the variants here:

  * [Original](http://wealthfrontinvite.com/)
  * [Referral](http://wealthfrontinvite.com/referral.html)
  * [Invite](http://wealthfrontinvite.com/invite.html)
  * [Affiliate](http://wealthfrontinvite.com/affiliate.html)
  * [Go](http://wealthfrontinvite.com/go.html)
  * [Coupon Code](http://wealthfrontinvite.com/couponcode.html)

Step 4 was to set up the Content Experiment on Google. You can see the
settings as well as the different variations in the screenshot below. I then
had to paste another script into index.html which would tell Google Analytics
to randomize which page to load.

![Screen Shot 2015-04-02 at 10.26.05
PM](https://i0.wp.com/www.derekchristensen.com/wp-
content/uploads/2015/04/Screen-
Shot-2015-04-02-at-10.26.05-PM-1024x640.png?resize=940%2C588)

That was pretty much it! I kicked off the experiment and watched the results
come in.

It was clear almost immediately that the other domain names weren’t getting
much traffic. The numbers were initially higher, but have dropped off
substantially since then. The http://wealthfrontinvite.com traffic has
tripled, but I think a lot of that new traffic is actually bots. “Human”
traffic has remained consistent, around 100 unique sessions a month.

![Screen Shot 2015-04-02 at 10.30.25
PM](https://i0.wp.com/www.derekchristensen.com/wp-
content/uploads/2015/04/Screen-
Shot-2015-04-02-at-10.30.25-PM-1024x488.png?resize=940%2C448)

The original page was the winner for most of the experiment, but the
“[Referral](http://wealthfrontinvite.com/referral.html)” variation edged it
out the last week or two. Total experiment length was 55 days. There were 135
total experiment sessions. If you know your statistics, you know that it’s not
a big enough sample size to truly determine which is best. Google hadn’t
declared a winner yet. However, this is an imperfect little learning
experiment, so I’m not going to let that bother me.

![Screen Shot 2015-04-02 at 10.34.01
PM](https://i0.wp.com/www.derekchristensen.com/wp-
content/uploads/2015/04/Screen-
Shot-2015-04-02-at-10.34.01-PM-1024x215.png?resize=940%2C197)

I recently heard the CEO of [Stratabeat](http://stratabeat.com/), [Tom
Shapiro](https://twitter.com/TomShapiro), speak at the [WordPress Boston
Meetup](http://www.meetup.com/boston-wordpress-meetup/events/221240090/) about
the neuroscience of web conversions. His presentation was amazing and we
talked for a while afterward. One key takeaway was that for most small
companies, he recommends sticking to A/B testing (comparing only two options)
rather than multivariate testing (comparing more than two options). With
smaller traffic volumes, it leads to quicker decisions about what is effective
and what is not. Another takeaway was to send equal traffic to all variants
(rather than sending more to the variant that converts the best).

I’ve declared the “[Referral](http://wealthfrontinvite.com/referral.html)”
variant the winner this time. In the next experiment I’ll take another of
Mike’s suggestions and add a background photo with faces. Thoughts?
Suggestions?
