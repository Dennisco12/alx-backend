import { createQueue } from 'kue';

const queue = createQueue({name: 'push_notification_code'});

const job = queue.create('push_notification_code', {
  phoneNumber: '09035371162',
  message: 'Welcome back Dennis'
});

job.on('enqueue', function(id, type) {
  console.log('Notification job created:', job.id);
}).on('complete', function(result) {
  console.log('Notification job completed');
}).on('failed attempt', function(errorMessage, doneAttempts) {
  console.log('Notification job failed');
});
job.save();
