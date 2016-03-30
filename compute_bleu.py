#!/usr/bin/env python

# written by Adam Lopez

import optparse
import sys
import bleu

optparser = optparse.OptionParser()
optparser.add_option("-r", "--reference", dest="reference", default="data/dev.ref", help="Target language reference sentences")
(opts,_) = optparser.parse_args()

def bleu(input_string):
    ref = [line.strip().split() for line in open(opts.reference)]
    hyp = [line.strip().split() for line in input_string.split('\n')]

    stats = [0 for i in xrange(10)]
    for (r,h) in zip(ref, hyp):
        stats = [sum(scores) for scores in zip(stats, bleu.bleu_stats(h,r))]
    return bleu.bleu(stats)

def compute_bleu(theta):
    input_string = ""
    all_hyps = [pair.split(' ||| ') for pair in open(opts.input)]
    num_sents = len(all_hyps) / 100
    for s in xrange(0, num_sents):
      hyps_for_one_sent = all_hyps[s * 100:s * 100 + 100]
      (best_score, best) = (-1e300, '')
      for (num, hyp, feats) in hyps_for_one_sent:
        score = 0.0
        for feat in feats.split(' '):
          (k, v) = feat.split('=')
          score += weights[k] * float(v)
        if score > best_score:
          (best_score, best) = (score, hyp)
      try: 
        input_string += "%s\n" % best
      except (Exception):
        sys.exit(1)

    return bleu(input_string)
