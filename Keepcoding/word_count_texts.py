stopWords = """
x
y
your
yours
yourself
yourselves
you
yond
yonder
yon
ye
yet
z
zillion
j
u
umpteen
usually
us
username
uponed
upons
uponing
upon
ups
upping
upped
up
unto
until
unless
unlike
unliker
unlikest
under
underneath
use
used
usedest
r
rath
rather
rathest
rathe
re
relate
related
relatively
regarding
really
res
respecting
respectively
q
quite
que
qua
n
neither
neaths
neath
nethe
nethermost
necessary
necessariest
necessarier
never
nevertheless
nigh
nighest
nigher
nine
noone
nobody
nobodies
nowhere
nowheres
no
noes
nor
nos
no-one
none
not
notwithstanding
nothings
nothing
nathless
natheless
t
ten
tills
till
tilled
tilling
to
towards
toward
towardest
towarder
together
too
thy
thyself
thus
than
that
those
thou
though
thous
thouses
thoroughest
thorougher
thorough
thoroughly
thru
thruer
thruest
thro
through
throughout
throughest
througher
thine
this
thises
they
thee
the
then
thence
thenest
thener
them
themselves
these
therer
there
thereby
therest
thereafter
therein
thereupon
therefore
their
theirs
thing
things
three
two
o
oh
owt
owning
owned
own
owns
others
other
otherwise
otherwisest
otherwiser
of
often
oftener
oftenest
off
offs
offest
one
ought
oughts
our
ours
ourselves
ourself
out
outest
outed
outwith
outs
outside
over
overallest
overaller
overalls
overall
overs
or
orer
orest
on
oneself
onest
ons
onto
a
atween
at
athwart
atop
afore
afterward
afterwards
after
afterest
afterer
ain
an
any
anything
anybody
anyone
anyhow
anywhere
anent
anear
and
andor
another
around
ares
are
aest
aer
against
again
accordingly
abaft
abafter
abaftest
abovest
above
abover
abouter
aboutest
about
aid
amidst
amid
among
amongst
apartest
aparter
apart
appeared
appears
appear
appearing
appropriating
appropriate
appropriatest
appropriates
appropriater
appropriated
already
always
also
along
alongside
although
almost
all
allest
aller
allyou
alls
albeit
awfully
as
aside
asides
aslant
ases
astrider
astride
astridest
astraddlest
astraddler
astraddle
availablest
availabler
available
aughts
aught
vs
v
variousest
variouser
various
via
vis-a-vis
vis-a-viser
vis-a-visest
viz
very
veriest
verier
versus
k
g
go
gone
good
got
gotta
gotten
get
gets
getting
b
by
byandby
by-and-by
bist
both
but
buts
be
beyond
because
became
becomes
become
becoming
becomings
becominger
becomingest
behind
behinds
before
beforehand
beforehandest
beforehander
bettered
betters
better
bettering
betwixt
between
beneath
been
below
besides
beside
m
my
myself
mucher
muchest
much
must
musts
musths
musth
main
make
mayest
many
mauger
maugre
me
meanwhiles
meanwhile
mostly
most
moreover
more
might
mights
midst
midsts
h
huh
humph
he
hers
herself
her
hereby
herein
hereafters
hereafter
hereupon
hence
hadst
had
having
haves
have
has
hast
hardly
hae
hath
him
himself
hither
hitherest
hitherer
his
how-do-you-do
however
how
howbeit
howdoyoudo
hoos
hoo
w
woulded
woulding
would
woulds
was
wast
we
wert
were
with
withal
without
within
why
what
whatever
whateverer
whateverest
whatsoeverer
whatsoeverest
whatsoever
whence
whencesoever
whenever
whensoever
when
whenas
whether
wheen
whereto
whereupon
wherever
whereon
whereof
where
whereby
wherewithal
wherewith
whereinto
wherein
whereafter
whereas
wheresoever
wherefrom
which
whichever
whichsoever
whilst
while
whiles
whithersoever
whither
whoever
whosoever
whoso
whose
whomever
s
syne
syn
shalling
shall
shalled
shalls
shoulding
should
shoulded
shoulds
she
sayyid
sayid
said
saider
saidest
same
samest
sames
samer
saved
sans
sanses
sanserifs
sanserif
so
soer
soest
sobeit
someone
somebody
somehow
some
somewhere
somewhat
something
sometimest
sometimes
sometimer
sometime
several
severaler
severalest
serious
seriousest
seriouser
senza
send
sent
seem
seems
seemed
seemingest
seeminger
seemings
seven
summat
sups
sup
supping
supped
such
since
sine
sines
sith
six
stop
stopped
p
plaintiff
plenty
plenties
please
pleased
pleases
per
perhaps
particulars
particularly
particular
particularest
particularer
pro
providing
provides
provided
provide
probably
l
layabout
layabouts
latter
latterest
latterer
latterly
latters
lots
lotting
lotted
lot
lest
less
ie
ifs
if
i
info
information
itself
its
it
is
idem
idemer
idemest
immediate
immediately
immediatest
immediater
in
inwards
inwardest
inwarder
inward
inasmuch
into
instead
insofar
indicates
indicated
indicate
indicating
indeed
inc
f
fact
facts
fs
figupon
figupons
figuponing
figuponed
few
fewer
fewest
frae
from
failing
failings
five
furthers
furtherer
furthered
furtherest
further
furthering
furthermore
fourscore
followthrough
for
forwhy
fornenst
formerly
former
formerer
formerest
formers
forbye
forby
fore
forever
forer
fores
four
d
ddays
dday
do
doing
doings
doe
does
doth
downwarder
downwardest
downward
downwards
downs
done
doner
dones
donest
dos
dost
did
differentest
differenter
different
describing
describe
describes
described
despiting
despites
despited
despite
during
c
cum
circa
chez
cer
certain
certainest
certainer
cest
canst
cannot
cant
cants
canting
cantest
canted
co
could
couldst
comeon
comeons
come-ons
come-on
concerning
concerninger
concerningest
consequently
considering
e
eg
eight
either
even
evens
evenser
evensest
evened
evenest
ever
everyone
everything
everybody
everywhere
every
ere
each
et
etc
elsewhere
else
ex
excepted
excepts
except
excepting
exes
enough

"""

text = """
“I’m sure those are not the right words,” said poor Alice, and her eyes filled with tears again as she went on, “I must be Mabel after all, and I shall have to go and live in that poky little house, and have next to no toys to play with, and oh! ever so many lessons to learn! No, I’ve made up my mind about it; if I’m Mabel, I’ll stay down here! It’ll be no use their putting their heads down and saying ‘Come up again, dear!’ I shall only look up and say ‘Who am I then? Tell me that first, and then, if I like being that person, I’ll come up: if not, I’ll stay down here till I’m somebody else’—but, oh dear!” cried Alice, with a sudden burst of tears, “I do wish they would put their heads down! I am so very tired of being all alone here!”

As she said this she looked down at her hands, and was surprised to see that she had put on one of the Rabbit’s little white kid gloves while she was talking. “How can I have done that?” she thought. “I must be growing small again.” She got up and went to the table to measure herself by it, and found that, as nearly as she could guess, she was now about two feet high, and was going on shrinking rapidly: she soon found out that the cause of this was the fan she was holding, and she dropped it hastily, just in time to avoid shrinking away altogether.

“That was a narrow escape!” said Alice, a good deal frightened at the sudden change, but very glad to find herself still in existence; “and now for the garden!” and she ran with all speed back to the little door: but, alas! the little door was shut again, and the little golden key was lying on the glass table as before, “and things are worse than ever,” thought the poor child, “for I never was so small as this before, never! And I declare it’s too bad, that it is!”

As she said these words her foot slipped, and in another moment, splash! she was up to her chin in salt water. Her first idea was that she had somehow fallen into the sea, “and in that case I can go back by railway,” she said to herself. (Alice had been to the seaside once in her life, and had come to the general conclusion, that wherever you go to on the English coast you find a number of bathing machines in the sea, some children digging in the sand with wooden spades, then a row of lodging houses, and behind them a railway station.) However, she soon made out that she was in the pool of tears which she had wept when she was nine feet high.

“I wish I hadn’t cried so much!” said Alice, as she swam about, trying to find her way out. “I shall be punished for it now, I suppose, by being drowned in my own tears! That will be a queer thing, to be sure! However, everything is queer to-day.”

Just then she heard something splashing about in the pool a little way off, and she swam nearer to make out what it was: at first she thought it must be a walrus or hippopotamus, but then she remembered how small she was now, and she soon made out that it was only a mouse that had slipped in like herself.

“Would it be of any use, now,” thought Alice, “to speak to this mouse? Everything is so out-of-the-way down here, that I should think very likely it can talk: at any rate, there’s no harm in trying.” So she began: “O Mouse, do you know the way out of this pool? I am very tired of swimming about here, O Mouse!” (Alice thought this must be the right way of speaking to a mouse: she had never done such a thing before, but she remembered having seen in her brother’s Latin Grammar, “A mouse—of a mouse—to a mouse—a mouse—O mouse!”) The Mouse looked at her rather inquisitively, and seemed to her to wink with one of its little eyes, but it said nothing.

“Perhaps it doesn’t understand English,” thought Alice; “I daresay it’s a French mouse, come over with William the Conqueror.” (For, with all her knowledge of history, Alice had no very clear notion how long ago anything had happened.) So she began again: “Où est ma chatte?” which was the first sentence in her French lesson-book. The Mouse gave a sudden leap out of the water, and seemed to quiver all over with fright. “Oh, I beg your pardon!” cried Alice hastily, afraid that she had hurt the poor animal’s feelings. “I quite forgot you didn’t like cats.”

“Not like cats!” cried the Mouse, in a shrill, passionate voice. “Would you like cats if you were me?”

“Well, perhaps not,” said Alice in a soothing tone: “don’t be angry about it. And yet I wish I could show you our cat Dinah: I think you’d take a fancy to cats if you could only see her. She is such a dear quiet thing,” Alice went on, half to herself, as she swam lazily about in the pool, “and she sits purring so nicely by the fire, licking her paws and washing her face—and she is such a nice soft thing to nurse—and she’s such a capital one for catching mice—oh, I beg your pardon!” cried Alice again, for this time the Mouse was bristling all over, and she felt certain it must be really offended. “We won’t talk about her any more if you’d rather not.”

“We indeed!” cried the Mouse, who was trembling down to the end of his tail. “As if I would talk on such a subject! Our family always hated cats: nasty, low, vulgar things! Don’t let me hear the name again!”

“I won’t indeed!” said Alice, in a great hurry to change the subject of conversation. “Are you—are you fond—of—of dogs?” The Mouse did not answer, so Alice went on eagerly: “There is such a nice little dog near our house I should like to show you! A little bright-eyed terrier, you know, with oh, such long curly brown hair! And it’ll fetch things when you throw them, and it’ll sit up and beg for its dinner, and all sorts of things—I can’t remember half of them—and it belongs to a farmer, you know, and he says it’s so useful, it’s worth a hundred pounds! He says it kills all the rats and—oh dear!” cried Alice in a sorrowful tone, “I’m afraid I’ve offended it again!” For the Mouse was swimming away from her as hard as it could go, and making quite a commotion in the pool as it went.

So she called softly after it, “Mouse dear! Do come back again, and we won’t talk about cats or dogs either, if you don’t like them!” When the Mouse heard this, it turned round and swam slowly back to her: its face was quite pale (with passion, Alice thought), and it said in a low trembling voice, “Let us get to the shore, and then I’ll tell you my history, and you’ll understand why it is I hate cats and dogs.”

It was high time to go, for the pool was getting quite crowded with the birds and animals that had fallen into it: there were a Duck and a Dodo, a Lory and an Eaglet, and several other curious creatures. Alice led the way, and the whole party swam to the shore.

"""